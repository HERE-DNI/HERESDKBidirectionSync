---
title: "Untitled"
slug: "sdk-for-flutter-navigate-navigation-eventtextlistener-eventtextlistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- EventTextListener.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li>/sdk-for-flutter-navigate-navigation-eventtextlistener-class</li>
<li class="self-crumb">EventTextListener factory constructor</li>
</ol>
<div class="self-name">EventTextListener</div>
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
<div class="main-content" data-above-sidebar="navigation/EventTextListener-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>EventTextListener constructor</h1></div>
<section class="multi-line-signature">
EventTextListener(<wbr/><ol class="parameter-list single-line"> <li>void onEventTextUpdatedLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-navigation-eventtext-class</li>
</ol>)</li>
</ol>)
    </section>
<section class="desc markdown">
<p>This abstract class should be implemented in order to receive notifications
when text notifications are available from /sdk-for-flutter-navigate-navigation-navigator-class.</p>
<p>Multiple notifications
can be given for the same maneuver at different distances.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory EventTextListener(
  void Function(EventText) onEventTextUpdatedLambda,

) =&gt; EventTextListener$Lambdas(
  onEventTextUpdatedLambda,

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
<li>/sdk-for-flutter-navigate-navigation-eventtextlistener-class</li>
<li class="self-crumb">EventTextListener factory constructor</li>
</ol>
<h5>EventTextListener class</h5>
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
