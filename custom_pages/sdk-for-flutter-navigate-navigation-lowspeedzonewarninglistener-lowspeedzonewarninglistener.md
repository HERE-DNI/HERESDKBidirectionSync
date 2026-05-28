---
title: "LowSpeedZoneWarningListener constructor"
slug: "sdk-for-flutter-navigate-navigation-lowspeedzonewarninglistener-lowspeedzonewarninglistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- LowSpeedZoneWarningListener.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li>/sdk-for-flutter-navigate-navigation-lowspeedzonewarninglistener-class</li>
<li class="self-crumb">LowSpeedZoneWarningListener factory constructor</li>
</ol>
<div class="self-name">LowSpeedZoneWarningListener</div>
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
<div class="main-content" data-above-sidebar="navigation/LowSpeedZoneWarningListener-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>LowSpeedZoneWarningListener constructor</h1></div>
<section class="multi-line-signature">
LowSpeedZoneWarningListener(<wbr/><ol class="parameter-list single-line"> <li>void onLowSpeedZoneWarningUpdatedLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-navigation-lowspeedzonewarning-class</li>
</ol>)</li>
</ol>)
    </section>
<section class="desc markdown">
<p>This abstract class should be implemented in order to receive low speed zone warnings.</p>
<p><strong>Note:</strong> This is currently available <em>only</em> for Japan.
The low speed zone warner is a zone warner, which means that for a low speed zone there will <em>always</em>
be 3 warnings emitted, with the <code>LowSpeedZoneWarning.distance_type</code> set to <code>DistanceType.AHEAD</code>, <code>DistanceType.REACHED</code>
and lastly <code>DistanceType.PASSED</code> when the end of the low speed zone is passed.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory LowSpeedZoneWarningListener(
  void Function(LowSpeedZoneWarning) onLowSpeedZoneWarningUpdatedLambda,

) =&gt; LowSpeedZoneWarningListener$Lambdas(
  onLowSpeedZoneWarningUpdatedLambda,

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
<li>/sdk-for-flutter-navigate-navigation-lowspeedzonewarninglistener-class</li>
<li class="self-crumb">LowSpeedZoneWarningListener factory constructor</li>
</ol>
<h5>LowSpeedZoneWarningListener class</h5>
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
