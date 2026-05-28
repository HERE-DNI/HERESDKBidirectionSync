---
title: "setProfile abstract method"
slug: "sdk-for-flutter-navigate-navigation-speedbasedcamerabehavior-setprofile"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setProfile.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li>/sdk-for-flutter-navigate-navigation-speedbasedcamerabehavior-class</li>
<li class="self-crumb">setProfile abstract method</li>
</ol>
<div class="self-name">setProfile</div>
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
<div class="main-content" data-above-sidebar="navigation/SpeedBasedCameraBehavior-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>setProfile abstract method</h1></div>
<section class="multi-line-signature">
void
setProfile(<wbr/><ol class="parameter-list single-line"> <li>List&lt;<wbr/>/sdk-for-flutter-navigate-navigation-speedbasedcamerabehaviorprofilevalue-class&gt; profile</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Sets the profile.</p>
<p>The speed ranges within the profile can overlap in order to prevent oscillations between
adjacent levels.
Provided profile must satisfy following conditions:</p>
<ul>
<li>
<p>profile must not be empty</p>
</li>
<li>
<p>each speed range must be valid (fromMetersPerSecond must be less then toMetersPerSecond)</p>
</li>
<li>
<p>ranges must be sorted by fromMetersPerSecond and toMetersPerSecond</p>
</li>
<li>
<p>gaps between ranges are not allowed
Invalid profile will be rejected and error message logged with explanation of violated restriction.</p>
</li>
<li>
<p><code>profile</code> The new profile value.</p>
</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void setProfile(List&lt;SpeedBasedCameraBehaviorProfileValue&gt; profile);</code></pre>
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
<li>/sdk-for-flutter-navigate-navigation-speedbasedcamerabehavior-class</li>
<li class="self-crumb">setProfile abstract method</li>
</ol>
<h5>SpeedBasedCameraBehavior class</h5>
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
