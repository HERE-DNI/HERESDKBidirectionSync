---
title: "Untitled"
slug: "sdk-for-flutter-navigate-warner-warnerengine-getcustomwarningnotificationdistances"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- getCustomWarningNotificationDistances.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-warner-warner-library</li>
<li>/sdk-for-flutter-navigate-warner-warnerengine-class</li>
<li class="self-crumb">getCustomWarningNotificationDistances abstract method</li>
</ol>
<div class="self-name">getCustomWarningNotificationDistances</div>
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
<div class="main-content" data-above-sidebar="warner/WarnerEngine-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>getCustomWarningNotificationDistances abstract method</h1></div>
<section class="multi-line-signature">
/sdk-for-flutter-navigate-navigation-warningnotificationdistances-class
getCustomWarningNotificationDistances(<wbr/><ol class="parameter-list single-line"> <li>int customWarningType</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Returns the warning notification distances for the specified custom warning type.</p>
<p>Unlike /sdk-for-flutter-navigate-warner-warnerengine-getwarningnotificationdistances, which operates on a /sdk-for-flutter-navigate-navigation-warningtype,
this method targets a specific custom warning category identified by <code>WarnerEngine.getCustomWarningNotificationDistances.customWarningType</code>,
as defined in /sdk-for-flutter-navigate-warner-customwarning-customwarningtype and /sdk-for-flutter-navigate-warner-warning-customwarningtype.</p>
<ul>
<li><code>customWarningType</code> The identifier of the custom warning type for which the
notification distances are requested.</li>
</ul>
<p>Returns /sdk-for-flutter-navigate-navigation-warningnotificationdistances-class. The warning notification distances configured for the given <code>WarnerEngine.getCustomWarningNotificationDistances.customWarningType</code>.
If no distances have been explicitly set for this type, a default
/sdk-for-flutter-navigate-navigation-warningnotificationdistances-class value is returned.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">WarningNotificationDistances getCustomWarningNotificationDistances(int customWarningType);</code></pre>
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
<li>/sdk-for-flutter-navigate-warner-warnerengine-class</li>
<li class="self-crumb">getCustomWarningNotificationDistances abstract method</li>
</ol>
<h5>WarnerEngine class</h5>
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
