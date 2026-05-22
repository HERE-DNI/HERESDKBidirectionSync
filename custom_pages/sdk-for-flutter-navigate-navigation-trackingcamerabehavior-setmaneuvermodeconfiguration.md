---
title: "Untitled"
slug: "sdk-for-flutter-navigate-navigation-trackingcamerabehavior-setmaneuvermodeconfiguration"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setManeuverModeConfiguration.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li>/sdk-for-flutter-navigate-navigation-trackingcamerabehavior-class</li>
<li class="self-crumb">setManeuverModeConfiguration abstract method</li>
</ol>
<div class="self-name">setManeuverModeConfiguration</div>
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
<div class="main-content" data-above-sidebar="navigation/TrackingCameraBehavior-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>setManeuverModeConfiguration abstract method</h1></div>
<section class="multi-line-signature">
void
setManeuverModeConfiguration(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuvermodeconfiguration-class? maneuverModeConfiguration</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Sets the configuration for camera behavior near maneuvers.</p>
<p>Defines how the camera reacts to nearby maneuvers when
/sdk-for-flutter-navigate-navigation-trackingcamerabehavior-ismaneuverdetectionenabled is <code>true</code>. When set to <code>null</code>, the camera does
not react to maneuvers. The configuration must contain at least one rule to be valid.
Defaults to <code>null</code>.</p>
<ul>
<li><code>maneuverModeConfiguration</code> The maneuver mode configuration. Invalid configurations are rejected.</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void setManeuverModeConfiguration(TrackingCameraBehaviorManeuverModeConfiguration? maneuverModeConfiguration);</code></pre>
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
<li>/sdk-for-flutter-navigate-navigation-trackingcamerabehavior-class</li>
<li class="self-crumb">setManeuverModeConfiguration abstract method</li>
</ol>
<h5>TrackingCameraBehavior class</h5>
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
