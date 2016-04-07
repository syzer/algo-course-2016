const arr = [1, 3, 9, 2, 2]

console.log(
    arr.sort((a, b) =>
        arr.reduce((l, r) =>
            l + (r == b) - (r == a)
            , 1
        )
    )[0],
    arr
)
