# Disposable Email Generator and Receiver :email: :inbox_tray: :outbox_tray:

![Example Image](https://cdn.discordapp.com/attachments/900836003810533416/1137039690193707139/image.png)

## Description :pencil:
This Python script allows you to generate disposable emails and receive emails on them. It utilizes the `requests`, `colorama`, `os`, `json`, and `time` modules. By adding a previously generated email to the `config.json`, you can list and continue to receive emails on that address.

## Installation :gear:
1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies using `pip` from the `requirements.txt` file: pip install -r requirements.txt

## Usage :rocket:
1. Before running the script, make sure to set up your `config.json` file with a list of previously generated emails (if any).
2. Run the Python script using the following command:
3. Follow the on-screen instructions to generate and receive emails.

## Configuration :wrench:
1. Edit the `config.json` file to manage previously generated emails.
2. The `config.json` file should have the following structure:
```json
{
  "emails": [
    "example1@mail.com"
  ]
}
```

## License :page_with_curl:

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or create a pull request.
Support :sparkling_heart:

If you find this project helpful or interesting, give it a ⭐ to show your appreciation!
