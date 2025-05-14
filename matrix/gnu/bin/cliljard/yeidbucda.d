module matrix.gnu.bin.cliljard;

import std.stdio;
import std.array;
import std.string;

import std.math;

/** 
    *   `keep.init = magic;`:
        *   Assigning to `.init` is invalid.
        *   `magic`: This comes from the `(ref cure, body magic)` 
        * part, which suggests `magic` might be a type or a template 
        * parameter, not a value that can be assigned.
*/ 
export T[] magic(const char keep)(ref auto cure, body magic)
@safe @property @nogc
{
    R!keep = new cure[magic];
    if (R!keep != cure[magic]) {
        
    }
}