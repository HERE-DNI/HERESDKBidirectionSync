---
title: "Untitled"
slug: "sdk-for-flutter-navigate-navigation-interpolatedlocationlistener-interpolatedlocationlistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- InterpolatedLocationListener.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li>/sdk-for-flutter-navigate-navigation-interpolatedlocationlistener-class</li>
<li class="self-crumb">InterpolatedLocationListener factory constructor</li>
</ol>
<div class="self-name">InterpolatedLocationListener</div>
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
<div class="main-content" data-above-sidebar="navigation/InterpolatedLocationListener-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>InterpolatedLocationListener constructor</h1></div>
<section class="multi-line-signature">
InterpolatedLocationListener(<wbr/><ol class="parameter-list single-line"> <li>void onInterpolatedLocationUpdatedLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-core-location-class</li>
</ol>)</li>
</ol>)
    </section>
<section class="desc markdown">
<p>This abstract class should be implemented
in order to receive interpolated locations.</p>
<p>The interpolated locations are only provided between
/sdk-for-flutter-navigate-navigation-visualnavigator-startrendering and /sdk-for-flutter-navigate-navigation-visualnavigator-stoprendering calls and the application
is not running in the background.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory InterpolatedLocationListener(
  void Function(Location) onInterpolatedLocationUpdatedLambda,

) =&gt; InterpolatedLocationListener$Lambdas(
  onInterpolatedLocationUpdatedLambda,

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
<li>/sdk-for-flutter-navigate-navigation-interpolatedlocationlistener-class</li>
<li class="self-crumb">InterpolatedLocationListener factory constructor</li>
</ol>
<h5>InterpolatedLocationListener class</h5>
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
