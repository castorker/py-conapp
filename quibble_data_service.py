import os, errno
from pathlib import Path
import pickle
from quibble import Quibble


class QuibbleDataService:
    def __init__(self):
        self._quibbles = list()
        self._file_path = "./quibbles.dat"

        if Path(self._file_path).exists():
            file = open(self._file_path, 'rb')  # open the file where the pickled data has been stored
            self._quibbles = pickle.load(file)  # dump information from the file
            file.close()
        else:
            self.seed()  # seed with some initial data

    def seed(self):
        """
        Populates the list of the quibbles with an initial quibble
        """
        quibble = Quibble()
        quibble.id = 1
        quibble.text = "Old programmers never die, they just can't C as well."
        quibble.category = "Technology"
        self._quibbles.append(quibble)
        self.save()

    def save(self):
        """
        Saves list of the quibbles to a file in binary format
        """
        file = open(self._file_path, 'wb')  # open file to store data
        pickle.dump(self._quibbles, file)  # dump information to file
        file.close()

    def get_all(self):
        """
        Retrieves all the quibbles from the list
        :return: list of objects
        """
        return self._quibbles

    def get_by_id(self, id):
        """
        Retrieves a specific quibble by id from the list
        :param id: int - quibble identifier
        :return: quibble object found if exists
        """
        return  next((q for q in self._quibbles if q.id == id), None)

    def create(self, quibble):
        """
        Creates a new quibble and adds it to the list
        :param quibble: object
        :return: quibble object created
        """
        try:
            # get the last quibble id - todo: to be improved
            last_id = max(q.id for q in self._quibbles)
        except ValueError:
            last_id = 0
        quibble.id = last_id + 1
        self._quibbles.append(quibble)
        self.save()
        return quibble

    def update(self, quibble):
        """
        Updates an existing quibble
        :param quibble: object
        :return: quibble objects updated
        """
        found = next((q for q in self._quibbles if q.id == quibble.id), None)
        if found is not None:
            self._quibbles.remove(found)
            self._quibbles.append(quibble)
            self.save()
        return quibble

    def delete(self, quibble_id):
        """
        Deletes an existing quibble
        :param quibble_id: int - quibble identifier
        """
        found = next((q for q in self._quibbles if q.id == quibble_id), None)
        if found is not None:
            self._quibbles.remove(found)
            if self._quibbles:
                self.save()
            else:
                try:
                    os.remove(self._file_path) if os.path.exists(self._file_path) else None
                except OSError as e:
                    if e.errno != errno.ENOENT:  # errno.ENOENT = no such file or directory
                        raise Exception  # re-raise exception if a different error occurred
