import os
import sys

from tranqtube import app

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../")


if __name__ == '__main__':
	app.run(host="dev.localhost", port=5000, debug=True)
