---
title: "Untitled"
slug: "sdk-for-flutter-navigate-navigation-railwaycrossingwarninglistener-railwaycrossingwarninglistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RailwayCrossingWarningListener.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li>/sdk-for-flutter-navigate-navigation-railwaycrossingwarninglistener-class</li>
<li class="self-crumb">RailwayCrossingWarningListener factory constructor</li>
</ol>
<div class="self-name">RailwayCrossingWarningListener</div>
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
<div class="main-content" data-above-sidebar="navigation/RailwayCrossingWarningListener-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>RailwayCrossingWarningListener constructor</h1></div>
<section class="multi-line-signature">
RailwayCrossingWarningListener(<wbr/><ol class="parameter-list single-line"> <li>void onRailwayCrossingWarningUpdatedLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-navigation-railwaycrossingwarning-class</li>
</ol>)</li>
</ol>)
    </section>
<section class="desc markdown">
<p>This abstract class
should be implemented in order to receive railway crossing warnings.</p>
<p><strong>Note:</strong> The railway crossing warner can be either a zone warner or a point warner, depending
on whether the railroad crossing warning is given for a railroad crossing zone or just a point. This
means that for a railway crossing there will can be either 2 or 3 warnings emitted. In case the railroad
crossing is a zone warner then 3 warnings will be emitted with the <code>RailwayCrossingWarning.distance_type</code> set to <code>DistanceType.AHEAD</code>,
<code>DistanceType.REACHED</code> and lastly <code>DistanceType.PASSED</code> when the end of the railway crossing is passed. In
case the railroad crossing is a point warner then 2 warnings will be emitted with the <code>RailwayCrossingWarning.distance_type</code>
set to <code>DistanceType.AHEAD</code> and <code>DistanceType.PASSED</code> when the end of the railway crossing is passed.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory RailwayCrossingWarningListener(
  void Function(RailwayCrossingWarning) onRailwayCrossingWarningUpdatedLambda,

) =&gt; RailwayCrossingWarningListener$Lambdas(
  onRailwayCrossingWarningUpdatedLambda,

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
<li>/sdk-for-flutter-navigate-navigation-railwaycrossingwarninglistener-class</li>
<li class="self-crumb">RailwayCrossingWarningListener factory constructor</li>
</ol>
<h5>RailwayCrossingWarningListener class</h5>
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
