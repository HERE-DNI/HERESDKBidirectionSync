---
title: "distanceInMeters property"
slug: "sdk-for-flutter-navigate-navigation-eventtext-distanceinmeters"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- distanceInMeters.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li>/sdk-for-flutter-navigate-navigation-eventtext-class</li>
<li class="self-crumb">distanceInMeters property</li>
</ol>
<div class="self-name">distanceInMeters</div>
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
<div class="main-content" data-above-sidebar="navigation/EventText-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>distanceInMeters property</h1></div>
<section class="multi-line-signature">
        
        double
        distanceInMeters
<div class="features">getter/setter pair</div>
</section>
<section class="desc markdown">
<p>Distance in meters to the location of the event for which the text notification is given.</p>
<p><strong>Note:</strong> For greater distances, distance in kilometers is rounded to the nearest digit (0.5 or
greater rounds up, else down) to simplify the distance phrase in <code>ManeuverNotifications</code> texts
during navigation. Distance in miles is rounded to the nearest 0.5 step. For example, 3.5 kilometers
are rounded to 4 kilometers and the notification will begin with <code>After 4 kilometers...</code>. However,
3.5 miles are not rounded up and the notification will begin with <code>After three and a half miles...</code>.
Same for 3.7 miles, whereas 3.8 miles are rounded to 4 miles. Note that the measurement units itself
are defined in the <code>UnitSystem</code> class.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">double distanceInMeters;</code></pre>
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
<li>/sdk-for-flutter-navigate-navigation-eventtext-class</li>
<li class="self-crumb">distanceInMeters property</li>
</ol>
<h5>EventText class</h5>
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
