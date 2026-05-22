---
title: "Untitled"
slug: "sdk-for-flutter-navigate-navigation-speedwarninglistener-speedwarninglistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- SpeedWarningListener.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li>/sdk-for-flutter-navigate-navigation-speedwarninglistener-class</li>
<li class="self-crumb">SpeedWarningListener factory constructor</li>
</ol>
<div class="self-name">SpeedWarningListener</div>
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
<div class="main-content" data-above-sidebar="navigation/SpeedWarningListener-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>SpeedWarningListener constructor</h1></div>
<section class="multi-line-signature">
SpeedWarningListener(<wbr/><ol class="parameter-list single-line"> <li>void onSpeedWarningStatusChangedLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-navigation-speedwarningstatus</li>
</ol>)</li>
</ol>)
    </section>
<section class="desc markdown">
<p>This abstract class should be implemented in order to receive notifications
when a speed limit on a road is exceeded or driving speed is restored back to normal.</p>
<p><strong>Note:</strong>
The warnings issued by this abstract class
don't take into account any temporary special speed limits. See <code>SpeedLimitListener</code>.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory SpeedWarningListener(
  void Function(SpeedWarningStatus) onSpeedWarningStatusChangedLambda,

) =&gt; SpeedWarningListener$Lambdas(
  onSpeedWarningStatusChangedLambda,

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
<li>/sdk-for-flutter-navigate-navigation-speedwarninglistener-class</li>
<li class="self-crumb">SpeedWarningListener factory constructor</li>
</ol>
<h5>SpeedWarningListener class</h5>
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
