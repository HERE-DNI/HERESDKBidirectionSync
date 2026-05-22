---
title: "Untitled"
slug: "sdk-for-flutter-navigate-navigation-maneuverviewlaneassistance-maneuverviewlaneassistance"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- ManeuverViewLaneAssistance.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li>/sdk-for-flutter-navigate-navigation-maneuverviewlaneassistance-class</li>
<li class="self-crumb">ManeuverViewLaneAssistance constructor</li>
</ol>
<div class="self-name">ManeuverViewLaneAssistance</div>
<form class="search navbar-right" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-box" placeholder="Loading search..." type="text"/>
</form>
<div class="toggle" id="theme-button" title="Toggle brightness">
<label for="theme">
<input id="theme" type="checkbox" value="light-theme"/>

        dark_mode
      

        light_mode
      
</label>
</div>
</header>
<main>
<div class="main-content" data-above-sidebar="navigation/ManeuverViewLaneAssistance-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>ManeuverViewLaneAssistance constructor</h1></div>
<section class="multi-line-signature">
ManeuverViewLaneAssistance(<wbr/><ol class="parameter-list single-line"> <li>List&lt;<wbr/>/sdk-for-flutter-navigate-navigation-lane-class&gt; lanesForNextManeuver, </li>
<li>List&lt;<wbr/>/sdk-for-flutter-navigate-navigation-lane-class&gt; lanesForNextNextManeuver</li>
</ol>)
    </section>
<section class="desc markdown">
<p>Creates a new instance.</p>
<ul>
<li><code>lanesForNextManeuver</code> A list of lanes on the current road that leads to the upcoming maneuver.
The lanes are sorted from left to right: The lane at index 0 represents the leftmost lane and
the last index represents the rightmost lane.
This is valid for both right-hand and left-hand driving countries.
Contraflow lanes are not included in the list.
The list is guaranteed to be non-empty.
/sdk-for-flutter-navigate-navigation-roadattributes-isrightdrivingside indicates if this is a left-hand driving country or not.</li>
<li><code>lanesForNextNextManeuver</code> A list of lanes on the road that leads to the maneuver after the upcoming maneuver.
The lanes are sorted from left to right: The lane at index 0 represents the leftmost lane and
the last index represents the rightmost lane.
This is valid for both right-hand and left-hand driving countries.
Contraflow lanes are not included in the list.
/sdk-for-flutter-navigate-navigation-roadattributes-isrightdrivingside indicates if this is a left-hand driving country or not.
By default, this list is empty. It will be filled when the next two maneuvers are too
close to each other, or when the next two maneuvers are roundabout maneuvers.
Note: This notification is delivered at the same time as the /sdk-for-flutter-navigate-navigation-maneuverviewlaneassistance-lanesfornextmaneuver.
There is no separate maneuver notification on the second maneuver when two maneuvers are
are too close to each other.</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">ManeuverViewLaneAssistance(this.lanesForNextManeuver, this.lanesForNextNextManeuver);</code></pre>
</section>
</div> 
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">

<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li>/sdk-for-flutter-navigate-navigation-maneuverviewlaneassistance-class</li>
<li class="self-crumb">ManeuverViewLaneAssistance constructor</li>
</ol>
<h5>ManeuverViewLaneAssistance class</h5>
<div id="dartdoc-sidebar-left-content"></div>
</div>
<div class="sidebar sidebar-offcanvas-right" id="dartdoc-sidebar-right">
</div>
</main>
<footer>

    here_sdk
      4.26.0
  
</footer>



</div>
`
}</HTMLBlock>
