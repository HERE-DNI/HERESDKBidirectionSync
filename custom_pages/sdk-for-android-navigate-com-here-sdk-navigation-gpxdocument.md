---
title: "GPXDocument (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-gpxdocument"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- GPXDocument.html -->
<!DOCTYPE HTML>









<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-package-summary">com.here.sdk.navigation</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.navigation.GPXDocument</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">GPXDocument</span>
<span class="extends-implements">extends <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-nativebase" title="class in com.here">NativeBase</a></span></div>
<div class="block"><p>Use the GPXDocument to load the GPX file.
 Only track data is used from the GPX file format
 (see trkType at https://www.topografix.com/GPX/1/1/#type_trkType).
 Any unknown elements in the file are ignored.
 Any known element with an invalid value returns an error.
 Elevation values are ignored.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">

<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#%3Cinit%3E(java.lang.String,com.here.sdk.navigation.GPXOptions)">GPXDocument</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> gpxFilePath,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-gpxoptions" title="class in com.here.sdk.navigation">GPXOptions</a> options)</code></div>
<div class="col-last even-row-color">
<div class="block">Create a GPX document from a file.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#%3Cinit%3E(java.util.List)">GPXDocument</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-gpxtrack" title="class in com.here.sdk.navigation">GPXTrack</a>&gt; tracks)</code></div>
<div class="col-last odd-row-color">
<div class="block">Create a GPX document from a list of GPX tracks.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#addTrack(com.here.sdk.navigation.GPXTrack)">addTrack</a><wbr/>(<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-gpxtrack" title="class in com.here.sdk.navigation">GPXTrack</a> trackToAdd)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Add track to GPX document.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-gpxdocument" title="class in com.here.sdk.navigation">GPXDocument</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#fromString(java.lang.String,com.here.sdk.navigation.GPXOptions)">fromString</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> content,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-gpxoptions" title="class in com.here.sdk.navigation">GPXOptions</a> options)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Create a GPX document from a string.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-gpxtrack" title="class in com.here.sdk.navigation">GPXTrack</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#getTracks()">getTracks</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the tracks stored in this GPX document.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#save(java.lang.String)">save</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> gpxFilePath)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Saves the document to a file.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">

<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,com.here.sdk.navigation.GPXOptions)">
<h3>GPXDocument</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">GPXDocument</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> gpxFilePath,
 @NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-gpxoptions" title="class in com.here.sdk.navigation">GPXOptions</a> options)</span>
            throws <span class="exceptions"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div class="block"><p>Create a GPX document from a file.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>gpxFilePath</code> - <p>The path to the GPX file.</p></dd>
<dd><code>options</code> - <p>The options to customize reading.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - <p>Indicates what went wrong when the instantiation was attempted.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.util.List)">
<h3>GPXDocument</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">GPXDocument</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-gpxtrack" title="class in com.here.sdk.navigation">GPXTrack</a>&gt; tracks)</span></div>
<div class="block"><p>Create a GPX document from a list of GPX tracks.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>tracks</code> - <p>The list of tracks.</p></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">

<ul class="member-list">
<li>
<section class="detail" id="fromString(java.lang.String,com.here.sdk.navigation.GPXOptions)">
<h3>fromString</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-gpxdocument" title="class in com.here.sdk.navigation">GPXDocument</a></span> <span class="element-name">fromString</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> content,
 @NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-gpxoptions" title="class in com.here.sdk.navigation">GPXOptions</a> options)</span>
                              throws <span class="exceptions"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div class="block"><p>Create a GPX document from a string.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>content</code> - <p>The content of a GPX file as string.</p></dd>
<dd><code>options</code> - <p>The options to customize reading.</p></dd>
<dt>Returns:</dt>
<dd><p>An <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-gpxdocument" title="class in com.here.sdk.navigation"><code>GPXDocument</code></a> instance.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - <p>Indicates what went wrong when the instantiation was attempted.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="save(java.lang.String)">
<h3>save</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">save</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> gpxFilePath)</span></div>
<div class="block"><p>Saves the document to a file.
 For saving the <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#getTracks()"><code>getTracks()</code></a> modification before writing to a file, use <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-gpxtrackwriter" title="class in com.here.sdk.navigation"><code>GPXTrackWriter</code></a>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>gpxFilePath</code> - <p>The file path where the GPX document will be saved.</p></dd>
<dt>Returns:</dt>
<dd><p><code>True</code> if the document has been saved successfully.
     <code>False</code> if an error has been happened during saving.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addTrack(com.here.sdk.navigation.GPXTrack)">
<h3>addTrack</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addTrack</span><wbr/><span class="parameters">(@NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-gpxtrack" title="class in com.here.sdk.navigation">GPXTrack</a> trackToAdd)</span></div>
<div class="block"><p>Add track to GPX document.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>trackToAdd</code> - <p>track to add to GPX document</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTracks()">
<h3>getTracks</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-gpxtrack" title="class in com.here.sdk.navigation">GPXTrack</a>&gt;</span> <span class="element-name">getTracks</span>()</div>
<div class="block"><p>Gets the tracks stored in this GPX document.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The tracks stored in this GPX document.</p></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->
</main>





</div>
`
}</HTMLBlock>
