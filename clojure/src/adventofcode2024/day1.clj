(ns adventofcode2024.day1
   (:require [clojure.java.io :as io]
   [clojure.string :as str] )
   (:import (java.io BufferedReader FileReader))
  (:gen-class))


(defn read-line->num
  [filename line-fn]
   (with-open [rdr (clojure.java.io/reader filename)]
     (loop [output {}
            line-num 1]
       (if-let [line (.readLine rdr)]
         (recur (assoc output (line-fn line) line-num) (inc line-num))
         output)
       )))

(def data-file (io/file
                 (io/resource 
                   "day1/input_small.txt" )))  

(defn process-file 
  [file-name]
  (with-open [rdr (BufferedReader. (FileReader. file-name))]
    
    (doseq [line (line-seq rdr)
            parts (filter not-empty (str/split line #" "))]
      parts))
    )

(defn sum [values]
  (reduce + values))

(defn difference [x]
   (abs (- (first x) (second x))))

(defn calculate 
[list1 list2]
  (let [values (map difference
            (map vector (sort list1) (sort list2) ))]
    (sum values)
    )
)




