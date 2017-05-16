;; Example 8-puzzle task.

(define (problem eight-puzzle-example)

  (:domain sliding-tile)

  (:objects
   tile1 tile2 tile3 tile4 tile5 tile6 tile7 tile8
   row1 row2 row3
   col1 col2 col3)

  (:init
   (IS-TILE tile1)
   (IS-TILE tile2)
   (IS-TILE tile3)
   (IS-TILE tile4)
   (IS-TILE tile5)
   (IS-TILE tile6)
   (IS-TILE tile7)
   (IS-TILE tile8)
   (IS-ROW row1)
   (IS-ROW row2)
   (IS-ROW row3)
   (NEXT-ROW row1 row2)
   (NEXT-ROW row2 row3)
   (IS-COLUMN col1)
   (IS-COLUMN col2)
   (IS-COLUMN col3)
   (NEXT-COLUMN col1 col2)
   (NEXT-COLUMN col2 col3)

   ;; initial state: first (top) row, left-to-right
   (tile-at tile5 row1 col1)
   (tile-at tile8 row1 col2)
   (tile-at tile1 row1 col3)
   ;; initial state: second row, left-to-right
   (tile-at tile4 row2 col1)
   (is-blank row2 col2)
   (tile-at tile7 row2 col3)
   ;; initial state: third (bottom) row, left-to-right
   (tile-at tile2 row3 col1)
   (tile-at tile6 row3 col2)
   (tile-at tile3 row3 col3)
   )

  ;; goal state
  (:goal
   (and
    (tile-at tile1 row1 col1)
    (tile-at tile2 row1 col2)
    (tile-at tile3 row1 col3)
    (tile-at tile4 row2 col1)
    (tile-at tile5 row2 col2)
    (tile-at tile6 row2 col3)
    (tile-at tile7 row3 col1)
    (tile-at tile8 row3 col2)))
  )
