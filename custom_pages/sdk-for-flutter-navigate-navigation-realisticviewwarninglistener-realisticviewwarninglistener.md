---
title: "RealisticViewWarningListener constructor"
slug: "sdk-for-flutter-navigate-navigation-realisticviewwarninglistener-realisticviewwarninglistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RealisticViewWarningListener.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li>/sdk-for-flutter-navigate-navigation-realisticviewwarninglistener-class</li>
<li class="self-crumb">RealisticViewWarningListener factory constructor</li>
</ol>
<div class="self-name">RealisticViewWarningListener</div>
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
<div class="main-content" data-above-sidebar="navigation/RealisticViewWarningListener-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>RealisticViewWarningListener constructor</h1></div>
<section class="multi-line-signature">
RealisticViewWarningListener(<wbr/><ol class="parameter-list single-line"> <li>void onRealisticViewWarningUpdatedLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-navigation-realisticviewwarning-class</li>
</ol>)</li>
</ol>)
    </section>
<section class="desc markdown">
<p>This abstract class
should be implemented in order to receive realistic view warnings.</p>
<p>A /sdk-for-flutter-navigate-navigation-realisticviewwarning-class will not be given until the previous warning of that type has been passed.
For example, a route with /sdk-for-flutter-navigate-navigation-realisticviewwarning-class 120 meters and /sdk-for-flutter-navigate-navigation-realisticviewwarning-class 160 meters ahead,
the first /sdk-for-flutter-navigate-navigation-realisticviewwarning-distancetorealisticviewinmeters is 120 meters
and the next /sdk-for-flutter-navigate-navigation-realisticviewwarning-distancetorealisticviewinmeters is then 40 meters,
since that is the distance between the first and second warnings.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory RealisticViewWarningListener(
  void Function(RealisticViewWarning) onRealisticViewWarningUpdatedLambda,

) =&gt; RealisticViewWarningListener$Lambdas(
  onRealisticViewWarningUpdatedLambda,

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
<li>/sdk-for-flutter-navigate-navigation-realisticviewwarninglistener-class</li>
<li class="self-crumb">RealisticViewWarningListener factory constructor</li>
</ol>
<h5>RealisticViewWarningListener class</h5>
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
