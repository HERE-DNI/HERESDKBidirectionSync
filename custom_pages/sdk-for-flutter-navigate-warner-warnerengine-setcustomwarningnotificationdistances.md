---
title: "Untitled"
slug: "sdk-for-flutter-navigate-warner-warnerengine-setcustomwarningnotificationdistances"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setCustomWarningNotificationDistances.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-warner-warner-library</li>
<li>/sdk-for-flutter-navigate-warner-warnerengine-class</li>
<li class="self-crumb">setCustomWarningNotificationDistances abstract method</li>
</ol>
<div class="self-name">setCustomWarningNotificationDistances</div>
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
<h1>setCustomWarningNotificationDistances abstract method</h1></div>
<section class="multi-line-signature">
bool
setCustomWarningNotificationDistances(<wbr/><ol class="parameter-list single-line"> <li>int customWarningType, </li>
<li>/sdk-for-flutter-navigate-navigation-warningnotificationdistances-class warningNotificationDistances</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Sets the warning notification distances for the specified custom warning type.</p>
<p>Unlike /sdk-for-flutter-navigate-warner-warnerengine-setwarningnotificationdistances, which applies settings to a /sdk-for-flutter-navigate-navigation-warningtype,
this method allows configuring notification distances independently for each custom warning
category identified by <code>WarnerEngine.setCustomWarningNotificationDistances.customWarningType</code>, as defined in
/sdk-for-flutter-navigate-warner-customwarning-customwarningtype and /sdk-for-flutter-navigate-warner-warning-customwarningtype.</p>
<ul>
<li>
<p><code>customWarningType</code> The identifier of the custom warning type for which the
notification distances should be set.</p>
</li>
<li>
<p><code>warningNotificationDistances</code> The warning notification distances to be applied
for the specified <code>WarnerEngine.setCustomWarningNotificationDistances.customWarningType</code>.</p>
</li>
</ul>
<p>Returns <code>bool</code>. True if the distances were successfully set; false otherwise.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">bool setCustomWarningNotificationDistances(int customWarningType, WarningNotificationDistances warningNotificationDistances);</code></pre>
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
<li class="self-crumb">setCustomWarningNotificationDistances abstract method</li>
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
