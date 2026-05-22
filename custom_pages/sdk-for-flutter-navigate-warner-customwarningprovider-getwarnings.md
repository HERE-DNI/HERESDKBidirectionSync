---
title: "Untitled"
slug: "sdk-for-flutter-navigate-warner-customwarningprovider-getwarnings"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- getWarnings.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-warner-warner-library</li>
<li>/sdk-for-flutter-navigate-warner-customwarningprovider-class</li>
<li class="self-crumb">getWarnings abstract method</li>
</ol>
<div class="self-name">getWarnings</div>
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
<div class="main-content" data-above-sidebar="warner/CustomWarningProvider-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>getWarnings abstract method</h1></div>
<section class="multi-line-signature">
List&lt;<wbr/>/sdk-for-flutter-navigate-warner-customwarning-class&gt;
getWarnings(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-mapdata-segmentdata-class currentSegment, </li>
<li>/sdk-for-flutter-navigate-mapdata-segmentdata-class? previousSegment</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Returns a list of custom warnings for the given vehicle position.</p>
<p>This method evaluates the custom warning provider using the current
vehicle position on the electronic horizon and returns the resulting
custom warnings along with corresponding payload.</p>
<ul>
<li>
<p><code>currentSegment</code> Segment data representing the vehicle’s current
position on the electronic horizon.</p>
</li>
<li>
<p><code>previousSegment</code> Segment data representing the vehicle’s previous
position on the electronic horizon. This parameter may be null if no
previous position information is available.</p>
</li>
</ul>
<p>Returns <code>List&lt;CustomWarning&gt;</code>. A list of <code>CustomWarning</code> instances representing all applicable
custom warnings. The list may be empty if no warnings apply.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">List&lt;CustomWarning&gt; getWarnings(SegmentData currentSegment, SegmentData? previousSegment);</code></pre>
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
<li>/sdk-for-flutter-navigate-warner-warner-library</li>
<li>/sdk-for-flutter-navigate-warner-customwarningprovider-class</li>
<li class="self-crumb">getWarnings abstract method</li>
</ol>
<h5>CustomWarningProvider class</h5>
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
