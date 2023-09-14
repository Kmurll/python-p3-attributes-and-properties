class Person:
    approved_jobs = [
        "Admin", "Customer Service", "Human Resources", "ITC", "Production",
        "Legal", "Finance", "Sales", "General Management", "Research & Development",
        "Marketing", "Purchasing"
    ]

    def __init__(self, name='', job=''):
        self._name = name
        self._job = job

    def get_name(self):
        return self._name

    def set_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name.title()
        else:
            raise ValueError("Name must be a string between 1 and 25 characters.")

    def get_job(self):
        return self._job

    def set_job(self, job):
        if job in Person.approved_jobs:
            self._job = job
        else:
            raise ValueError("Job must be in the list of approved jobs.")

    name = property(get_name, set_name)
    job = property(get_job, set_job)
class Person:
    approved_jobs = [
        "Admin", "Customer Service", "Human Resources", "ITC", "Production",
        "Legal", "Finance", "Sales", "General Management", "Research & Development",
        "Marketing", "Purchasing"
    ]

    def __init__(self, name='', job=''):
        self._name = name
        self._job = job

    def get_name(self):
        return self._name

    def set_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name.title()
        else:
            raise ValueError("Name must be a string between 1 and 25 characters.")

    def get_job(self):
        return self._job

    def set_job(self, job):
        if job in Person.approved_jobs:
            self._job = job
        else:
            raise ValueError("Job must be in the list of approved jobs.")

    name = property(get_name, set_name)
    job = property(get_job, set_job)
