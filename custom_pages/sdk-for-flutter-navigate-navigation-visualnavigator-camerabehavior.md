---
title: "cameraBehavior property"
slug: "sdk-for-flutter-navigate-navigation-visualnavigator-camerabehavior"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- cameraBehavior.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li>/sdk-for-flutter-navigate-navigation-visualnavigator-class</li>
<li class="self-crumb">cameraBehavior property</li>
</ol>
<div class="self-name">cameraBehavior</div>
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
<div class="main-content" data-above-sidebar="navigation/VisualNavigator-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>cameraBehavior property</h1></div>
<section id="getter">
<section class="multi-line-signature">
/sdk-for-flutter-navigate-navigation-camerabehavior-class?
cameraBehavior
</section>
<section class="desc markdown">
<p>Camera behavior which defines how the /sdk-for-flutter-navigate-navigation-visualnavigator-class handles the camera.
Setting <code>null</code> disables any camera behavior with the result that the camera does not follow
the current location and keeps the last active camera state, i.e., current zoom and tilt.
Furthermore, when <code>null</code> is set map gestures can be used again to freely pan and zoom
the map. In opposition, when a camera behavior is defined, then the map cannot be panned and
zoomed by the user.
The default value is an instance of /sdk-for-flutter-navigate-navigation-fixedcamerabehavior-class.
Gets the currently set camera behavior.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">CameraBehavior? get cameraBehavior;</code></pre>
</section>
</section>
<section id="setter">
<section class="multi-line-signature">
void
cameraBehavior=(<wbr/>/sdk-for-flutter-navigate-navigation-camerabehavior-class? value)
</section>
<section class="desc markdown">
<p>Camera behavior which defines how the /sdk-for-flutter-navigate-navigation-visualnavigator-class handles the camera.
Setting <code>null</code> disables any camera behavior with the result that the camera does not follow
the current location and keeps the last active camera state, i.e., current zoom and tilt.
Furthermore, when <code>null</code> is set map gestures can be used again to freely pan and zoom
the map. In opposition, when a camera behavior is defined, then the map cannot be panned and
zoomed by the user.
The default value is an instance of /sdk-for-flutter-navigate-navigation-fixedcamerabehavior-class.
Sets how the VisualNavigator handles the camera.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">set cameraBehavior(CameraBehavior? value);</code></pre>
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
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li>/sdk-for-flutter-navigate-navigation-visualnavigator-class</li>
<li class="self-crumb">cameraBehavior property</li>
</ol>
<h5>VisualNavigator class</h5>
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
