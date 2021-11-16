package com.praisecapital.project_x.core

import org.scalatest.funsuite.AnyFunSuite
import com.praisecapital.project_x.model._
import com.praisecapital.project_x.core.CoreComputation
import scala.collection.mutable.LinkedHashMap
import com.praisecapital.project_x.model.{
  ModelADefaultObject,
  ModelBDefaultObject
}

class CoreComputationUnitTests extends AnyFunSuite {
  test("Can compute") {
    val coreComputation = new CoreComputation()
    assert(List(ComputationResult(1, "", 1)) === coreComputation.compute(List(ModelADefaultObject.copy())))
  }
}
