# Safeout: write out a file safely

With `safeout`, you can write:

    from safeout import safeout
    with safeout('output.txt') as output:
        output.write("Hello world\n")

and this will write out the file `output.txt` in a safe, atomic manner. That
is, if there are any problems (Exceptions or a crash) in the `with` block, then
there there will be **no output**. If the `with` block completes, then the
output file will include the whole result.

So, if the output file exists, you can be confident that the process completed
correctly.

License: MIT

