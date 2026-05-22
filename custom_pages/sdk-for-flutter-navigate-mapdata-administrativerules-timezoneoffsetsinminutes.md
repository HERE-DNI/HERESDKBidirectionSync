---
title: "Untitled"
slug: "sdk-for-flutter-navigate-mapdata-administrativerules-timezoneoffsetsinminutes"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- timeZoneOffsetsInMinutes.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapdata-mapdata-library</li>
<li>/sdk-for-flutter-navigate-mapdata-administrativerules-class</li>
<li class="self-crumb">timeZoneOffsetsInMinutes property</li>
</ol>
<div class="self-name">timeZoneOffsetsInMinutes</div>
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
<div class="main-content" data-above-sidebar="mapdata/AdministrativeRules-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>timeZoneOffsetsInMinutes property</h1></div>
<section class="multi-line-signature">
        
        List&lt;<wbr/>Duration&gt;
timeZoneOffsetsInMinutes
<div class="features">getter/setter pair</div>
</section>
<section class="desc markdown">
<p>The time zone offset from UTC of the country or state expressed in minutes. The value can also be negative
(e.g.: Eastern Standard Time (EST) will be -360 minutes, Central European Time (CET) will be 60 minutes).
Defaults to 0 minutes.
<strong>Note:</strong> A time zone with a positive shift of 1 hour and 30 minutes will result in a time zone offset of
90 minutes. A time zone with a negative shift of 3 hour and 30 minutes will result in an time zone offset
of -210 minutes. In order to properly calculate the time zone offset, the <code>AdministrativeRules.daylight_saving_period</code>
should be taken into consideration and if the daylight savings time is observed at the time of the
calculation, then a value of 60 minutes should be substracted from the time zone offset.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">List&lt;Duration&gt; timeZoneOffsetsInMinutes;</code></pre>
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
<li>/sdk-for-flutter-navigate-mapdata-administrativerules-class</li>
<li class="self-crumb">timeZoneOffsetsInMinutes property</li>
</ol>
<h5>AdministrativeRules class</h5>
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
