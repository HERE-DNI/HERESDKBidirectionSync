---
title: "Untitled"
slug: "sdk-for-flutter-navigate-navigation-junctionviewlaneassistance-lanesfornextjunction"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- lanesForNextJunction.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li>/sdk-for-flutter-navigate-navigation-junctionviewlaneassistance-class</li>
<li class="self-crumb">lanesForNextJunction property</li>
</ol>
<div class="self-name">lanesForNextJunction</div>
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
<div class="main-content" data-above-sidebar="navigation/JunctionViewLaneAssistance-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>lanesForNextJunction property</h1></div>
<section class="multi-line-signature">
        
        List&lt;<wbr/>/sdk-for-flutter-navigate-navigation-lane-class&gt;
lanesForNextJunction
<div class="features">getter/setter pair</div>
</section>
<section class="desc markdown">
<p>A list of lanes on the next complex junction.
The lanes are sorted from left to right: The lane at index 0 represents the leftmost lane and
the last index represents the rightmost lane. This is valid for right-hand and left-hand driving
countries. An empty list means that the complex junction has been passed and that the lane information is not
valid anymore. Exactly one event with a non-empty list is delivered before reaching a complex junction and
one event with an empty list afterwards.</p>
<p><strong>Note:</strong> Lanes going in opposite direction are not included in the list.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">List&lt;Lane&gt; lanesForNextJunction;</code></pre>
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
<li>/sdk-for-flutter-navigate-navigation-junctionviewlaneassistance-class</li>
<li class="self-crumb">lanesForNextJunction property</li>
</ol>
<h5>JunctionViewLaneAssistance class</h5>
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
