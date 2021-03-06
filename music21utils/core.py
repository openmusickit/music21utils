# AUTOGENERATED! DO NOT EDIT! File to edit: 00_core.ipynb (unless otherwise specified).

__all__ = ['create_stream']

# Cell
import music21 as m

# Cell
def create_stream(
    stream_type: type[m.stream.Stream],
    stream_info: dict={},
    *pass_args,
    **pass_kwargs
) -> m.stream.Stream:
    s = stream_type()
    for key, val in stream_info.items():
        setattr(s, key, val)
    return s
