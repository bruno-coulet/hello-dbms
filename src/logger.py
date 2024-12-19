import json
import os

class Logger:
    def __init__(self, log_file):
        self.log_file = log_file
        self.logs = {
            "steps": [],
            "errors": []
        }
        self._ensure_log_file()

    def _ensure_log_file(self):
        """Vérifie si le fichier de log existe et crée un fichier vide si nécessaire."""
        if not os.path.exists(self.log_file):
            with open(self.log_file, 'w') as log:
                json.dump(self.logs, log, indent=4)

    def log_step(self, category, message, success=True):
        """
        Ajoute un log pour une étape.
        :param category: Catégorie du log (ex. "Table Creation").
        :param message: Message détaillé de l'étape (peut être une chaîne de caractères ou un dictionnaire structuré).
        :param success: Indique si l'opération a réussi (True ou False).
        """
        # Si le message est déjà un dictionnaire structuré, on l'ajoute directement
        if isinstance(message, dict):
            log_entry = {
                "category": category,
                "message": message,
                "success": success
            }
        else:
            # Sinon, c'est une chaîne de texte classique
            log_entry = {
                "category": category,
                "message": message,
                "success": success
            }
        
        # Ajouter l'entrée au log
        self.logs["steps"].append(log_entry)
        self.save_logs()

    def log_error(self, category, message):
        """
        Ajoute un log pour une erreur.
        :param category: Catégorie de l'erreur.
        :param message: Message d'erreur détaillé.
        """
        self.logs["errors"].append({
            "category": category,
            "message": message
        })
        self.save_logs()

    def save_logs(self):
        """Enregistre les logs dans le fichier."""
        with open(self.log_file, 'w') as log:
            json.dump(self.logs, log, indent=4)
