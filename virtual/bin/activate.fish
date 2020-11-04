<<<<<<< HEAD
# This file must be used with ". bin/activate.fish" *from fish* (http://fishshell.org)
# you cannot run it directly

function deactivate  -d "Exit virtualenv and return to normal shell environment"
=======
# This file must be used using `. bin/activate.fish` *within a running fish ( http://fishshell.com ) session*.
# Do not run it directly.

function deactivate -d 'Exit virtualenv mode and return to the normal environment.'
>>>>>>> bb5cd4133aa4d74f0947126e999ea138279514d4
    # reset old environment variables
    if test -n "$_OLD_VIRTUAL_PATH"
        set -gx PATH $_OLD_VIRTUAL_PATH
        set -e _OLD_VIRTUAL_PATH
    end
<<<<<<< HEAD
=======

>>>>>>> bb5cd4133aa4d74f0947126e999ea138279514d4
    if test -n "$_OLD_VIRTUAL_PYTHONHOME"
        set -gx PYTHONHOME $_OLD_VIRTUAL_PYTHONHOME
        set -e _OLD_VIRTUAL_PYTHONHOME
    end

    if test -n "$_OLD_FISH_PROMPT_OVERRIDE"
<<<<<<< HEAD
        functions -e fish_prompt
        set -e _OLD_FISH_PROMPT_OVERRIDE
        functions -c _old_fish_prompt fish_prompt
        functions -e _old_fish_prompt
    end

    set -e VIRTUAL_ENV
    if test "$argv[1]" != "nondestructive"
        # Self destruct!
=======
        # Set an empty local `$fish_function_path` to allow the removal of `fish_prompt` using `functions -e`.
        set -l fish_function_path

        # Erase virtualenv's `fish_prompt` and restore the original.
        functions -e fish_prompt
        functions -c _old_fish_prompt fish_prompt
        functions -e _old_fish_prompt
        set -e _OLD_FISH_PROMPT_OVERRIDE
    end

    set -e VIRTUAL_ENV

    if test "$argv[1]" != 'nondestructive'
        # Self-destruct!
        functions -e pydoc
>>>>>>> bb5cd4133aa4d74f0947126e999ea138279514d4
        functions -e deactivate
    end
end

<<<<<<< HEAD
# unset irrelevant variables
deactivate nondestructive

set -gx VIRTUAL_ENV "/home/andrew-john/Documents/rental/kikiz-property-management-software/virtual"
=======
# Unset irrelevant variables.
deactivate nondestructive

set -gx VIRTUAL_ENV "/home/moringa/Documents/Moringa-Projects/CORE-PYTHON/kikiz-property-management-software/virtual"
>>>>>>> bb5cd4133aa4d74f0947126e999ea138279514d4

set -gx _OLD_VIRTUAL_PATH $PATH
set -gx PATH "$VIRTUAL_ENV/bin" $PATH

<<<<<<< HEAD
# unset PYTHONHOME if set
=======
# Unset `$PYTHONHOME` if set.
>>>>>>> bb5cd4133aa4d74f0947126e999ea138279514d4
if set -q PYTHONHOME
    set -gx _OLD_VIRTUAL_PYTHONHOME $PYTHONHOME
    set -e PYTHONHOME
end

<<<<<<< HEAD
if test -z "$VIRTUAL_ENV_DISABLE_PROMPT"
    # fish uses a function instead of an env var to generate the prompt.

    # save the current fish_prompt function as the function _old_fish_prompt
    functions -c fish_prompt _old_fish_prompt

    # with the original prompt function renamed, we can override with our own.
    function fish_prompt
        # Save the return status of the last command
        set -l old_status $status

        # Prompt override?
        if test -n "(virtual) "            
            printf "%s%s" "(virtual) " (set_color normal)
        else
            # ...Otherwise, prepend env
            set -l _checkbase (basename "$VIRTUAL_ENV")
            if test $_checkbase = "__"
                # special case for Aspen magic directories
                # see http://www.zetadev.com/software/aspen/
                printf "%s[%s]%s " (set_color -b blue white) (basename (dirname "$VIRTUAL_ENV")) (set_color normal)
            else
                printf "%s(%s)%s" (set_color -b blue white) (basename "$VIRTUAL_ENV") (set_color normal)
            end
        end

        # Restore the return status of the previous command.
        echo "exit $old_status" | .
=======
function pydoc
    python -m pydoc $argv
end

if test -z "$VIRTUAL_ENV_DISABLE_PROMPT"
    # Copy the current `fish_prompt` function as `_old_fish_prompt`.
    functions -c fish_prompt _old_fish_prompt

    function fish_prompt
        # Save the current $status, for fish_prompts that display it.
        set -l old_status $status

        # Prompt override provided?
        # If not, just prepend the environment name.
        if test -n ""
            printf '%s%s' "" (set_color normal)
        else
            printf '%s(%s) ' (set_color normal) (basename "$VIRTUAL_ENV")
        end

        # Restore the original $status
        echo "exit $old_status" | source
>>>>>>> bb5cd4133aa4d74f0947126e999ea138279514d4
        _old_fish_prompt
    end

    set -gx _OLD_FISH_PROMPT_OVERRIDE "$VIRTUAL_ENV"
end
