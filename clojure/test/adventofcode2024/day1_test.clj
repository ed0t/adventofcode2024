(ns adventofcode2024.day1-test
  (:require [clojure.test :refer :all]
            [adventofcode2024.day1 :refer :all]))


(deftest calculate-test
  (testing "compute distance"
    (is (= (calculate [1 8 3] [4 3 2]) 5))))
