---
title: "RDSEncryptionKey class"
slug: "sdk-for-flutter-navigate-trafficbroadcast-rdsencryptionkey-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RDSEncryptionKey-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="trafficbroadcast/RDSEncryptionKey-class.html#constructors">Constructors</a></li>
<li><a href="trafficbroadcast/RDSEncryptionKey/RDSEncryptionKey.html">RDSEncryptionKey</a></li>
<li class="section-title">
<a href="trafficbroadcast/RDSEncryptionKey-class.html#instance-properties">Properties</a>
</li>
<li><a href="trafficbroadcast/RDSEncryptionKey/encryptionId.html">encryptionId</a></li>
<li class="inherited"><a href="trafficbroadcast/RDSEncryptionKey/hashCode.html">hashCode</a></li>
<li><a href="trafficbroadcast/RDSEncryptionKey/rotateRight.html">rotateRight</a></li>
<li class="inherited"><a href="trafficbroadcast/RDSEncryptionKey/runtimeType.html">runtimeType</a></li>
<li><a href="trafficbroadcast/RDSEncryptionKey/startBit.html">startBit</a></li>
<li><a href="trafficbroadcast/RDSEncryptionKey/xorValue.html">xorValue</a></li>
<li class="section-title inherited"><a href="trafficbroadcast/RDSEncryptionKey-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="trafficbroadcast/RDSEncryptionKey/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="trafficbroadcast/RDSEncryptionKey/toString.html">toString</a></li>
<li class="section-title inherited"><a href="trafficbroadcast/RDSEncryptionKey-class.html#operators">Operators</a></li>
<li class="inherited"><a href="trafficbroadcast/RDSEncryptionKey/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-trafficbroadcast-trafficbroadcast-library</li>
<li class="self-crumb">RDSEncryptionKey class</li>
</ol>
<div class="self-name">RDSEncryptionKey</div>
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
<div class="main-content" data-above-sidebar="trafficbroadcast/trafficbroadcast-library-sidebar.html" data-below-sidebar="trafficbroadcast/RDSEncryptionKey-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>RDSEncryptionKey class</h1></div>
<section class="desc markdown">
<p>Represents the RDS encryption key.</p>
<p>Fields allocation information is described in CEN ISO/CD 14819-6.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="RDSEncryptionKey">
/sdk-for-flutter-navigate-trafficbroadcast-rdsencryptionkey-rdsencryptionkey(int encryptionId, int rotateRight, int startBit, int xorValue)
</dt>
<dd>
          Creates a new instance.
        </dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="encryptionId">
/sdk-for-flutter-navigate-trafficbroadcast-rdsencryptionkey-encryptionid
↔ int
</dt>
<dd>
  Id of encryption key within the list.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-trafficbroadcast-rdsencryptionkey-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="rotateRight">
/sdk-for-flutter-navigate-trafficbroadcast-rdsencryptionkey-rotateright
↔ int
</dt>
<dd>
  Rotate Right used for bit manipulations as a part of encryption process.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-trafficbroadcast-rdsencryptionkey-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="startBit">
/sdk-for-flutter-navigate-trafficbroadcast-rdsencryptionkey-startbit
↔ int
</dt>
<dd>
  Start Bit used for bit manipulations as a part of encryption process.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="xorValue">
/sdk-for-flutter-navigate-trafficbroadcast-rdsencryptionkey-xorvalue
↔ int
</dt>
<dd>
  XOR Value used for bit manipulations as a part of encryption process.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-trafficbroadcast-rdsencryptionkey-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-trafficbroadcast-rdsencryptionkey-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-trafficbroadcast-rdsencryptionkey-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-navigate-trafficbroadcast-trafficbroadcast-library</li>
<li class="self-crumb">RDSEncryptionKey class</li>
</ol>
<h5>trafficbroadcast library</h5>
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
