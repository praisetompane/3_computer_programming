package com.praisecapital.project_x.core

import scala.collection.mutable.LinkedHashMap
import com.praisecapital.project_x.model._

class CoreComputation() {
  def compute(modelAs: List[ModelA]): List[ComputationResult] = {
    //modelAs.map{modelA => do stuff with modelA}
    List(ComputationResult(1, "", 1))
  }
}
