---
title: "SegmentSpecialSpeedSituation constructor"
slug: "sdk-for-flutter-navigate-mapdata-segmentspecialspeedsituation-segmentspecialspeedsituation"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- SegmentSpecialSpeedSituation.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapdata-mapdata-library</li>
<li>/sdk-for-flutter-navigate-mapdata-segmentspecialspeedsituation-class</li>
<li class="self-crumb">SegmentSpecialSpeedSituation constructor</li>
</ol>
<div class="self-name">SegmentSpecialSpeedSituation</div>
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
<div class="main-content" data-above-sidebar="mapdata/SegmentSpecialSpeedSituation-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>SegmentSpecialSpeedSituation constructor</h1></div>
<section class="multi-line-signature">
SegmentSpecialSpeedSituation(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-mapdata-specialspeedtype specialSpeedType, </li>
<li>double speedLimitInMetersPerSecond, </li>
<li>List&lt;<wbr/>/sdk-for-flutter-navigate-core-timerule-class&gt; appliesDuring</li>
</ol>)
    </section>
<section class="desc markdown">
<p>Creates a new instance with default values.</p>
<ul>
<li><code>specialSpeedType</code> Represents the speed situation type.</li>
<li><code>speedLimitInMetersPerSecond</code> Overrides normal speed limit for this situation.</li>
</ul>
<p>May be 0 to indicate no special speed limit in the case of special_speed_type = SPEED_BUMPS_PRESENT
and special_speed_type = LANE_DEPENDENT.
Speed limit in meter per seconds.</p>
<ul>
<li><code>appliesDuring</code> The times during which the condition applies.
May be empty for all special_speed_type values except <code>TIME_DEPENDENT</code> and <code>APPROXIMATE_SEASONAL_TIME</code>.</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">SegmentSpecialSpeedSituation(this.specialSpeedType, this.speedLimitInMetersPerSecond, this.appliesDuring);</code></pre>
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
<li>/sdk-for-flutter-navigate-mapdata-mapdata-library</li>
<li>/sdk-for-flutter-navigate-mapdata-segmentspecialspeedsituation-class</li>
<li class="self-crumb">SegmentSpecialSpeedSituation constructor</li>
</ol>
<h5>SegmentSpecialSpeedSituation class</h5>
<div id="dartdoc-sidebar-left-content"></div>
</div>
<div class="sidebar sidebar-offcanvas-right" id="dartdoc-sidebar-right">
</div>
</main>
<footer>

    here_sdk
      4.26.0
  
</footer>
</div></div>
</div>
`
}</HTMLBlock>
