# PseudoTerm

Run pseudo-commands from the terminal with the power of ChatGPT. Converts your pseudo-command or mistyped command into an actual command that can be run in the terminal.

## Usage

```console
$ ./gpt.py [your pseudo command]
```

## API Key

You need to add your OpenAI API key to the `OPENAI_API_KEY` environment variable.

Linux:
```console
$ export OPENAI_API_KEY=YOUR_API_KEY
```

Windows:
```console
> set OPENAI_API_KEY=YOUR_API_KEY
```

## Examples

```console
$ ./gpt.py find -type mkv avi mp4 +1G
COMMAND: find -type f \( -name "*.mkv" -o -name "*.avi" -o -name "*.mp4" \) -size +1G
Run? (y/n)
```

```console
$ ./gpt.py find "*.py" -containing "except:" -linenumbers -filenames
COMMAND: find . -name "*.py" -exec grep -n "except:" {} +
Run? (y/n)
```

```console
$ ./gpt.py git revert 3 commits
COMMAND: git revert HEAD~3
Run? (y/n)
```
