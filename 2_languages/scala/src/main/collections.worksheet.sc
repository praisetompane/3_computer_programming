import scala.collection.mutable.LinkedHashMap
case class LeagueRank(rank: Int, teamName: String, points: Int)

val pointsTable = LinkedHashMap(
  "Tarantulas" -> 6,
  "Lions" -> 5,
  "Snakes" -> 1,
  "FC Awesome" -> 1,
  "Grouches" -> 0
)

/*
    group team points entries, by points
    sort by points in decreasing order
    from the top
        assign rank to each team
            starting from 1

            if group has more than 1 entry
                sort alphabetically
                assign same rank to all teams in group

 */

//def retrieveRankings(): LinkedHashMap[String, Int] = {

def sortByNameAlphabetically(teamA: (String, Int), teamB: (String, Int)) = {
  val (teamAName, _) = teamA
  val (teamBName, _) = teamB
  teamAName < teamBName
}

def sortByPointsDescendingOrder(
    pointsGroup_1: (Int, LinkedHashMap[String, Int]),
    pointsGroup_2: (Int, LinkedHashMap[String, Int])
) = {
  val (groupApoints, groupAteams) = pointsGroup_1
  val (groupBpoints, groupBteams) = pointsGroup_2
  groupApoints > groupBpoints
}

val leaguePointsGroupsDescendingOrderByPoints = pointsTable
  .groupBy { case (_, points) => points }
  .toSeq
  .sortWith(sortByPointsDescendingOrder)

val internalPointsGroupsAlphabeticalOrder =
  leaguePointsGroupsDescendingOrderByPoints.map { case (points, pointsGroups) =>
    val p = pointsGroups
    p.toSeq.sortWith(sortByNameAlphabetically)
  }

var nextRank = 1
var leagueRank = scala.collection.mutable.Seq()
internalPointsGroupsAlphabeticalOrder.map { case pointsGroup =>
  leagueRank ++ pointsGroup.map { case (teamName, points) =>
    LeagueRank(nextRank + leagueRank.length, teamName, points)
  }
}

val indexZipped = internalPointsGroupsAlphabeticalOrder.zipWithIndex

indexZipped
/*rank algorithm
  first pointsgroup rank = 1
  currentRankToUse = pointsGroup index + 1 (zip is zero indexed)
                     number of elements(teams) in the previous points group

                     NB: teams in higher points groups take up a rank
                         in the rank count, even though they're not assinged it, beacuse they have the same points.





 */
indexZipped.map { case (pointsGroups, index) =>
  pointsGroups.map { case (teamName, points) =>
    LeagueRank(
      index + { if (index != 0) indexZipped(index - 1)._1.length else 1 },
      teamName,
      points
    )
  }
}.flatten

/*val rank = 1
  val teamsWithRank = sortedPointsGroupsAlpha.map { case (teamName, points) =>
    (rank, teamName, points)
  }
  val a = teamsWithRank*/
/*grouped.zipWithIndex
    .map { case (pointsGroup, index) =>
      pointsGroup._2.toSeq.sortWith(sortByPointsThenName: _*)
    }
    .map { case (teamName, points) => LeagueRank(index + 1, teamName, points) }
    .flatten

  println(grouped)
  grouped*/
//val sortedRankings = LinkedHashMap(pointsTable.toSeq.sortWith(sortByPointsThenName): _*)
//sortedRankings
/*Allocate same rank to team if they have same points
      The sort alphabetically
 */

//}
