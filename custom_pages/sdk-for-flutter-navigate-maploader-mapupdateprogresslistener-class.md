---
title: "Untitled"
slug: "sdk-for-flutter-navigate-maploader-mapupdateprogresslistener-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapUpdateProgressListener-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-maploader-maploader-library</li>
<li class="self-crumb">MapUpdateProgressListener class</li>
</ol>
<div class="self-name">MapUpdateProgressListener</div>
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
<div class="main-content" data-above-sidebar="maploader/maploader-library-sidebar.html" data-below-sidebar="maploader/MapUpdateProgressListener-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>MapUpdateProgressListener class abstract</h1></div>
<section class="desc markdown">
<p>Abstract class to get notified on status updates
when updating map data, previously downloaded by /sdk-for-flutter-navigate-maploader-mapdownloader-class.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="MapUpdateProgressListener">
/sdk-for-flutter-navigate-maploader-mapupdateprogresslistener-mapupdateprogresslistener(void onProgressLambda(/sdk-for-flutter-navigate-maploader-regionid-class, int), void onPauseLambda(/sdk-for-flutter-navigate-maploader-maploadererror?), void onCompleteLambda(/sdk-for-flutter-navigate-maploader-maploadererror?), void onResumeLambda())
</dt>
<dd>
          Abstract class to get notified on status updates
when updating map data, previously downloaded by /sdk-for-flutter-navigate-maploader-mapdownloader-class.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-maploader-mapupdateprogresslistener-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-maploader-mapupdateprogresslistener-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-maploader-mapupdateprogresslistener-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="onComplete">
/sdk-for-flutter-navigate-maploader-mapupdateprogresslistener-oncomplete(<wbr/>/sdk-for-flutter-navigate-maploader-maploadererror? error)
    → void

</dt>
<dd>
  Called after the update process for all regions has been completed.
  

</dd>
<dt class="callable" id="onPause">
/sdk-for-flutter-navigate-maploader-mapupdateprogresslistener-onpause(<wbr/>/sdk-for-flutter-navigate-maploader-maploadererror? error)
    → void

</dt>
<dd>
  Called when update is paused.
  

</dd>
<dt class="callable" id="onProgress">
/sdk-for-flutter-navigate-maploader-mapupdateprogresslistener-onprogress(<wbr/>/sdk-for-flutter-navigate-maploader-regionid-class region, int percentage)
    → void

</dt>
<dd>
  Called multiple times to indicate the update progress.
  

</dd>
<dt class="callable" id="onResume">
/sdk-for-flutter-navigate-maploader-mapupdateprogresslistener-onresume(<wbr/>)
    → void

</dt>
<dd>
  Called when a paused map update is resumed.
  

</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-maploader-mapupdateprogresslistener-tostring(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="operators">
<h2>Operators</h2>
<dl class="callables">
<dt class="callable inherited" id="operator ==">
/sdk-for-flutter-navigate-maploader-mapupdateprogresslistener-operator-equals(<wbr/>Object other)
    → bool

</dt>
<dd class="inherited">
  The equality operator.
  <div class="features">inherited</div>
</dd>
</dl>
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
<li class="self-crumb">MapUpdateProgressListener class</li>
</ol>
<h5>maploader library</h5>
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
