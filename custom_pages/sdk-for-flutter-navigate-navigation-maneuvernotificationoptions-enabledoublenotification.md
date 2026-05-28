---
title: "enableDoubleNotification property"
slug: "sdk-for-flutter-navigate-navigation-maneuvernotificationoptions-enabledoublenotification"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- enableDoubleNotification.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li>/sdk-for-flutter-navigate-navigation-maneuvernotificationoptions-class</li>
<li class="self-crumb">enableDoubleNotification property</li>
</ol>
<div class="self-name">enableDoubleNotification</div>
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
<div class="main-content" data-above-sidebar="navigation/ManeuverNotificationOptions-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>enableDoubleNotification property</h1></div>
<section class="multi-line-signature">
        
        bool
        enableDoubleNotification
<div class="features">getter/setter pair</div>
</section>
<section class="desc markdown">
<p>A flag that indicates whether combined maneuver notifications should be generated.
Such double notifications can be useful when maneuvers are very close.
<strong>Example:</strong> A combined message: 'After 300 meters turn left and then turn right.'.
This way a user can better anticipate the next-next maneuver.
Note that setting to <code>true</code> will make the notification longer as two maneuvers will be merged into one.
When the next-next maneuver action takes place, the notification will be given as usual.
<strong>Example:</strong> 'Now turn left and then then turn right.' will be followed by 'Now turn right.'.
Defaults to <code>true</code>.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">bool enableDoubleNotification;</code></pre>
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
<li>/sdk-for-flutter-navigate-navigation-maneuvernotificationoptions-class</li>
<li class="self-crumb">enableDoubleNotification property</li>
</ol>
<h5>ManeuverNotificationOptions class</h5>
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
