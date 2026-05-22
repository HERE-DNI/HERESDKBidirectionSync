---
title: "Untitled"
slug: "sdk-for-flutter-navigate-maploader-mapupdater-taskcount"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- taskCount.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-maploader-maploader-library</li>
<li>/sdk-for-flutter-navigate-maploader-mapupdater-class</li>
<li class="self-crumb">taskCount property</li>
</ol>
<div class="self-name">taskCount</div>
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
<div class="main-content" data-above-sidebar="maploader/MapUpdater-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>taskCount property</h1></div>
<section id="getter">
<section class="multi-line-signature">
int
taskCount
</section>
<section class="desc markdown">
<p>The number of concurrent tasks for downloading a map.
A valid task count is between 1 to 64. When the value set is outside the valid range,
then it is clamped to a valid range:</p>
<ul>
<li>when passed in value is 0 or less, then task count is set to 1;</li>
<li>when passed in value is 65 or more, then task count is set to 64.
Gets the number of concurrent tasks for downloading a map.</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">int get taskCount;</code></pre>
</section>
</section>
<section id="setter">
<section class="multi-line-signature">
void
taskCount=(<wbr/>int value)
</section>
<section class="desc markdown">
<p>The number of concurrent tasks for downloading a map.
A valid task count is between 1 to 64. When the value set is outside the valid range,
then it is clamped to a valid range:</p>
<ul>
<li>when passed in value is 0 or less, then task count is set to 1;</li>
<li>when passed in value is 65 or more, then task count is set to 64.
Sets the number of concurrent tasks for downloading a map.</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">set taskCount(int value);</code></pre>
</section>
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
<li>/sdk-for-flutter-navigate-maploader-maploader-library</li>
<li>/sdk-for-flutter-navigate-maploader-mapupdater-class</li>
<li class="self-crumb">taskCount property</li>
</ol>
<h5>MapUpdater class</h5>
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
