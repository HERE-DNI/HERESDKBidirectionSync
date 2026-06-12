---
title: "CurrentSituationLaneAssistanceViewListener class abstract"
slug: "sdk-for-flutter-navigate-navigation-currentsituationlaneassistanceviewlistener-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- CurrentSituationLaneAssistanceViewListener-class.html -->


<div>
<h1>CurrentSituationLaneAssistanceViewListener class abstract</h1></div>

<p>This abstract class should be
implemented in order to receive notifications on <a href="/sdk-for-flutter-navigate-navigation-currentsituationlaneassistanceview-class">CurrentSituationLaneAssistanceView</a>.</p>
<p>The current situation lane assistance view notifications describe the lane information at the current location.</p>
<p>A new notification is evaluated with each location update. A notification is only sent when there is a change
in lane data, such as a new upcoming lane.</p>
<p>This event is supported both with a route during turn-by-turn navigation and without a route in tracking mode.
During turn-by-turn navigation, the event additionally indicates which lanes help the driver stay on the route
to reach the destination.
However, the event does not indicate which exact lane the user is currently driving in.
The listener works for offline mode as well.</p>
<p><strong>Note:</strong></p>
<ul>
<li>Lane information is not available for all roads. It's mostly available for roads with painted turn directions.</li>
<li>This is a <strong>beta</strong> release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</li>
</ul>


<h2>Constructors</h2>
<ul><li><a href="/sdk-for-flutter-navigate-navigation-currentsituationlaneassistanceviewlistener-currentsituationlaneassistanceviewlistener">CurrentSituationLaneAssistanceViewListener</a></li></ul>


<h2>Properties</h2>
<ul><li><a href="/sdk-for-flutter-navigate-navigation-currentsituationlaneassistanceviewlistener-hashcode">hashCode</a></li><li><a href="/sdk-for-flutter-navigate-navigation-currentsituationlaneassistanceviewlistener-runtimetype">runtimeType</a></li></ul>


<h2>Methods</h2>
<ul><li><a href="/sdk-for-flutter-navigate-navigation-currentsituationlaneassistanceviewlistener-nosuchmethod">noSuchMethod</a></li><li><a href="/sdk-for-flutter-navigate-navigation-currentsituationlaneassistanceviewlistener-oncurrentsituationlaneassistanceviewupdate">onCurrentSituationLaneAssistanceViewUpdate</a></li><li><a href="/sdk-for-flutter-navigate-navigation-currentsituationlaneassistanceviewlistener-tostring">toString</a></li></ul>


<h2>Operators</h2>
<ul><li><a href="/sdk-for-flutter-navigate-navigation-currentsituationlaneassistanceviewlistener-operator-equals">operator ==</a></li></ul>

 



</div>
`
}</HTMLBlock>
