Unfortunately, my attempt at improving the performance was not very
successful, so I didn't keep many changes. There weren't many options I could
think of to get rid of the nested loops or the amount of numbers that have to
be multiplied without using numpy (tried zip, list comprehension, but didn't
help)
Worst offending lines are the ones that use random to create X and Y and the
two last multiplication lines (where all elements are individually multiplied)
Memory usage was also difficult to alter since X,Y and result need to be
stored and all of the functions are only referencing and altering these as far
as I could see. So I think this is slightly above me.
