---
title: "milestoneStatusListener property"
slug: "sdk-for-flutter-navigate-navigation-navigatorinterface-milestonestatuslistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- milestoneStatusListener.html -->


<div>
<h1>milestoneStatusListener property</h1></div>
<section id="getter">

<a href="/sdk-for-flutter-navigate-navigation-milestonestatuslistener-class">MilestoneStatusListener</a>?
milestoneStatusListener


<p>Object to receive notifications about the arrival at each <a href="/sdk-for-flutter-navigate-navigation-milestone-class">Milestone</a> or missing it.
It informs on all waypoints (passed or missed) that
are of type <a href="/sdk-for-flutter-navigate-navigation-milestonetype">MilestoneType.stopover</a> but excludes the
starting waypoint.
Waypoints of type <a href="/sdk-for-flutter-navigate-navigation-milestonetype">MilestoneType.passthrough</a> are excluded, by default,
but can be included via <a href="/sdk-for-flutter-navigate-navigation-navigatorinterface-ispassthroughwaypointshandlingenabled">NavigatorInterface.isPassthroughWaypointsHandlingEnabled</a>.
Milestone status notifications only occurs if a route has been set.
Setting <code>null</code> value to the listener will unset the listener.
It returns <code>null</code> when no listener is set by an user.
Gets the listener that notifies when a <a href="/sdk-for-flutter-navigate-navigation-milestone-class">Milestone</a> has been reached or missed.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">MilestoneStatusListener? get milestoneStatusListener;</code></pre>

</section>
<section id="setter">

void
milestoneStatusListener=(<a href="/sdk-for-flutter-navigate-navigation-milestonestatuslistener-class">MilestoneStatusListener</a>? value)


<p>Object to receive notifications about the arrival at each <a href="/sdk-for-flutter-navigate-navigation-milestone-class">Milestone</a> or missing it.
It informs on all waypoints (passed or missed) that
are of type <a href="/sdk-for-flutter-navigate-navigation-milestonetype">MilestoneType.stopover</a> but excludes the
starting waypoint.
Waypoints of type <a href="/sdk-for-flutter-navigate-navigation-milestonetype">MilestoneType.passthrough</a> are excluded, by default,
but can be included via <a href="/sdk-for-flutter-navigate-navigation-navigatorinterface-ispassthroughwaypointshandlingenabled">NavigatorInterface.isPassthroughWaypointsHandlingEnabled</a>.
Milestone status notifications only occurs if a route has been set.
Setting <code>null</code> value to the listener will unset the listener.
It returns <code>null</code> when no listener is set by an user.
Sets the listener that notifies when a <a href="/sdk-for-flutter-navigate-navigation-milestone-class">Milestone</a> has been reached or missed.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">set milestoneStatusListener(MilestoneStatusListener? value);</code></pre>

</section>
 



</div>
`
}</HTMLBlock>
