---
title: "LaneDecreaseWarning class"
slug: "sdk-for-flutter-navigate-warner-lanedecreasewarning-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- LaneDecreaseWarning-class.html -->


<div>
<h1>LaneDecreaseWarning class</h1></div>

<p>Represents a lane decrease warning that notifies about upcoming reductions in the number of available lanes.</p>
<p>Lane decrease warnings are generated when the road ahead has fewer lanes
than the previous road segment provided by <code>sdk.electronic_horizon.ElectronicHorizonEngine</code>,
requiring drivers to merge or change lanes.
Lane decrease is provided only on highways and motorways. It will not be provided for junctions,
when maneuver is given for the lane decrease situation or when the <a href="/sdk-for-flutter-navigate-navigation-trafficmergewarning-class">TrafficMergeWarning</a>
is provided. Special lanes (e.g. Bus lane, HOV) will only be included to the lane decrease warning generation
if the according options are set in <a href="/sdk-for-flutter-navigate-transport-transportspecification-class">TransportSpecification</a>.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>


<h2>Constructors</h2>
<ul><li><a href="/sdk-for-flutter-navigate-warner-lanedecreasewarning-lanedecreasewarning">LaneDecreaseWarning</a></li></ul>


<h2>Properties</h2>
<ul><li><a href="/sdk-for-flutter-navigate-warner-lanedecreasewarning-distanceinmeters">distanceInMeters</a></li><li><a href="/sdk-for-flutter-navigate-warner-lanedecreasewarning-distancetype">distanceType</a></li><li><a href="/sdk-for-flutter-navigate-warner-lanedecreasewarning-hashcode">hashCode</a></li><li><a href="/sdk-for-flutter-navigate-warner-lanedecreasewarning-id">id</a></li><li><a href="/sdk-for-flutter-navigate-warner-lanedecreasewarning-lanesdecreasedfromleft">lanesDecreasedFromLeft</a></li><li><a href="/sdk-for-flutter-navigate-warner-lanedecreasewarning-lanesdecreasedfromright">lanesDecreasedFromRight</a></li><li><a href="/sdk-for-flutter-navigate-warner-lanedecreasewarning-newlanenumber">newLaneNumber</a></li><li><a href="/sdk-for-flutter-navigate-warner-lanedecreasewarning-previouslanenumber">previousLaneNumber</a></li><li><a href="/sdk-for-flutter-navigate-warner-lanedecreasewarning-runtimetype">runtimeType</a></li></ul>


<h2>Methods</h2>
<ul><li><a href="/sdk-for-flutter-navigate-warner-lanedecreasewarning-nosuchmethod">noSuchMethod</a></li><li><a href="/sdk-for-flutter-navigate-warner-lanedecreasewarning-tostring">toString</a></li></ul>


<h2>Operators</h2>
<ul><li><a href="/sdk-for-flutter-navigate-warner-lanedecreasewarning-operator-equals">operator ==</a></li></ul>

 



</div>
`
}</HTMLBlock>
