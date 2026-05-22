---
title: "Untitled"
slug: "sdk-for-flutter-navigate-routing-maxspeedonsegment-maxspeedonsegment"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MaxSpeedOnSegment.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-routing-routing-library</li>
<li>/sdk-for-flutter-navigate-routing-maxspeedonsegment-class</li>
<li class="self-crumb">MaxSpeedOnSegment constructor</li>
</ol>
<div class="self-name">MaxSpeedOnSegment</div>
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
<div class="main-content" data-above-sidebar="routing/MaxSpeedOnSegment-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>MaxSpeedOnSegment constructor</h1></div>
<section class="multi-line-signature">
MaxSpeedOnSegment(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-routing-segmentreference-class segment, </li>
<li>double baseSpeedInMetersPerSecond</li>
</ol>)
    </section>
<section class="desc markdown">
<p>Creates a new instance.</p>
<ul>
<li><code>segment</code> A segment for which the new base speed is specified. Only the <code>segmendId</code> and <code>travelDirection</code>
parameters are used, other parameters are ignored. Setting a <code>segmendId</code> is mandatory.</li>
</ul>
<p><strong>Note:</strong> The <code>SegmentReference</code> is not directly accessible from the map via the HERE SDK.
Although, after route calculation you can retrieve the related segments for each /sdk-for-flutter-navigate-routing-span-class.
The segment IDs are the same that are also used by, for example, the <a href="https://www.here.com/docs/bundle/routing-api-developer-guide-v8/page/topics/use-cases/avoid-segments.html">Routing REST API</a>.
These IDs are mostly stable and only change when the underlying map data changes
due to a new road or similar changes in the real world.</p>
<ul>
<li><code>baseSpeedInMetersPerSecond</code> New maximum value in m/s of baseSpeed on segment.  The provided value must be in the range [1.0, 70.0].
Cannot increase base speed on segment. If the value is greater than the default base speed, then such penalty will have no effect.</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">MaxSpeedOnSegment(this.segment, this.baseSpeedInMetersPerSecond);</code></pre>
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
<li>/sdk-for-flutter-navigate-routing-routing-library</li>
<li>/sdk-for-flutter-navigate-routing-maxspeedonsegment-class</li>
<li class="self-crumb">MaxSpeedOnSegment constructor</li>
</ol>
<h5>MaxSpeedOnSegment class</h5>
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
