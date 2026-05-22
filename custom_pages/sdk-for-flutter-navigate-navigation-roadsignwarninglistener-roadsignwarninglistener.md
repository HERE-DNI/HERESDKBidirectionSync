---
title: "Untitled"
slug: "sdk-for-flutter-navigate-navigation-roadsignwarninglistener-roadsignwarninglistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RoadSignWarningListener.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li>/sdk-for-flutter-navigate-navigation-roadsignwarninglistener-class</li>
<li class="self-crumb">RoadSignWarningListener factory constructor</li>
</ol>
<div class="self-name">RoadSignWarningListener</div>
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
<div class="main-content" data-above-sidebar="navigation/RoadSignWarningListener-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>RoadSignWarningListener constructor</h1></div>
<section class="multi-line-signature">
RoadSignWarningListener(<wbr/><ol class="parameter-list single-line"> <li>void onRoadSignWarningUpdatedLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-navigation-roadsignwarning-class</li>
</ol>)</li>
</ol>)
    </section>
<section class="desc markdown">
<p>This abstract class
should be implemented in order to receive road sign warnings.</p>
<p><strong>Note:</strong> The road sign warner is a point warner, which means that for a road sign there will <em>always</em> be
2 warnings emitted, with the /sdk-for-flutter-navigate-navigation-roadsignwarning-distancetype set to /sdk-for-flutter-navigate-navigation-distancetype and /sdk-for-flutter-navigate-navigation-distancetype
which is given when the location of the road sign is reached.
A /sdk-for-flutter-navigate-navigation-roadsignwarning-class will not be given until the previous warning of that type has been passed.
For example, a route with /sdk-for-flutter-navigate-navigation-roadsignwarning-class 120 meters and /sdk-for-flutter-navigate-navigation-roadsignwarning-class 160 meters ahead,
the first /sdk-for-flutter-navigate-navigation-roadsignwarning-distancetoroadsigninmeters is 120 meters
and the next /sdk-for-flutter-navigate-navigation-roadsignwarning-distancetoroadsigninmeters is then 40 meters,
since that is the distance between the first and second warnings.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory RoadSignWarningListener(
  void Function(RoadSignWarning) onRoadSignWarningUpdatedLambda,

) =&gt; RoadSignWarningListener$Lambdas(
  onRoadSignWarningUpdatedLambda,

);</code></pre>
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
<li>/sdk-for-flutter-navigate-navigation-roadsignwarninglistener-class</li>
<li class="self-crumb">RoadSignWarningListener factory constructor</li>
</ol>
<h5>RoadSignWarningListener class</h5>
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
