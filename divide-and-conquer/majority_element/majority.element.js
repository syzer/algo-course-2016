const arr = [2, 3, 9, 2, 2]
console.log(
    arr.sort((a, b) =>
        arr.reduce((l, r) =>
            l + (r == b) - (r == a)
            , 0
        )
    )[0],
    arr
)
