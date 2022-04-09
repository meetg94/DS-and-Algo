function oceanHeights(heights) {
    let res = []
    for (let i = 0; i < heights.length; i++) {
        let oceanView = true
        for (let j=i+1; j < heights.length; j++) {
            if (heights[i] < heights[j]) {
                oceanView = false
    }
    }
        if (oceanView === true) {
            res.push(i)
        }
}
return res
}

console.log(oceanHeights([4,3,2,1]))