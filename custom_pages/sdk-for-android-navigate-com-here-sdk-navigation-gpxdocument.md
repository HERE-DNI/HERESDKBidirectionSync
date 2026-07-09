---
title: "GPXDocument (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-gpxdocument"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- GPXDocument.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.navigation</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.navigation.GPXDocument</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">GPXDocument</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>Use the GPXDocument to load the GPX file.
 Only track data is used from the GPX file format
 (see trkType at https://www.topografix.com/GPX/1/1/#type_trkType).
 Any unknown elements in the file are ignored.
 Any known element with an invalid value returns an error.
 Elevation values are ignored.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-gpxdocument#%3Cinit%3E(java.lang.String,com.here.sdk.navigation.GPXOptions)">GPXDocument</a><wbr/>(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> gpxFilePath,
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-gpxoptions" title="class in com.here.sdk.navigation">GPXOptions</a> options)</code></div>
<div className="col-last even-row-color">
<div className="block">Create a GPX document from a file.</div>
</div>
<div className="col-constructor-name odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-gpxdocument#%3Cinit%3E(java.util.List)">GPXDocument</a><wbr/>(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-gpxtrack" title="class in com.here.sdk.navigation">GPXTrack</a>&gt; tracks)</code></div>
<div className="col-last odd-row-color">
<div className="block">Create a GPX document from a list of GPX tracks.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section className="method-summary" id="method-summary">

<div id="method-summary-table">


</div>
<div className="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section className="details">
<ul className="details-list">
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section className="constructor-details" id="constructor-detail">

<ul className="member-list">
<li>
<section className="detail" id="&lt;init&gt;(java.lang.String,com.here.sdk.navigation.GPXOptions)">
<h3>GPXDocument</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">GPXDocument</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> gpxFilePath,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-gpxoptions" title="class in com.here.sdk.navigation">GPXOptions</a> options)</span>
            throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div className="block"><p>Create a GPX document from a file.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>gpxFilePath</code> - <p>The path to the GPX file.</p></dd>
<dd><code>options</code> - <p>The options to customize reading.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - <p>Indicates what went wrong when the instantiation was attempted.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(java.util.List)">
<h3>GPXDocument</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">GPXDocument</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-gpxtrack" title="class in com.here.sdk.navigation">GPXTrack</a>&gt; tracks)</span></div>
<div className="block"><p>Create a GPX document from a list of GPX tracks.</p></div>
<dl className="notes">
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
<section className="method-details" id="method-detail">

<ul className="member-list">
<li>
<section className="detail" id="fromString(java.lang.String,com.here.sdk.navigation.GPXOptions)">
<h3>fromString</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-gpxdocument" title="class in com.here.sdk.navigation">GPXDocument</a></span> <span className="element-name">fromString</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> content,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-gpxoptions" title="class in com.here.sdk.navigation">GPXOptions</a> options)</span>
                              throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div className="block"><p>Create a GPX document from a string.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>content</code> - <p>The content of a GPX file as string.</p></dd>
<dd><code>options</code> - <p>The options to customize reading.</p></dd>
<dt>Returns:</dt>
<dd><p>An <a href="sdk-for-android-navigate-com-here-sdk-navigation-gpxdocument" title="class in com.here.sdk.navigation"><code>GPXDocument</code></a> instance.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - <p>Indicates what went wrong when the instantiation was attempted.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="save(java.lang.String)">
<h3>save</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">save</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> gpxFilePath)</span></div>
<div className="block"><p>Saves the document to a file.
 For saving the <a href="sdk-for-android-navigate-com-here-sdk-navigation-gpxdocument#getTracks()"><code>getTracks()</code></a> modification before writing to a file, use <a href="sdk-for-android-navigate-com-here-sdk-navigation-gpxtrackwriter" title="class in com.here.sdk.navigation"><code>GPXTrackWriter</code></a>.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>gpxFilePath</code> - <p>The file path where the GPX document will be saved.</p></dd>
<dt>Returns:</dt>
<dd><p><code>True</code> if the document has been saved successfully.
     <code>False</code> if an error has been happened during saving.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="addTrack(com.here.sdk.navigation.GPXTrack)">
<h3>addTrack</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">addTrack</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-gpxtrack" title="class in com.here.sdk.navigation">GPXTrack</a> trackToAdd)</span></div>
<div className="block"><p>Add track to GPX document.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>trackToAdd</code> - <p>track to add to GPX document</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getTracks()">
<h3>getTracks</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-gpxtrack" title="class in com.here.sdk.navigation">GPXTrack</a>&gt;</span> <span className="element-name">getTracks</span>()</div>
<div className="block"><p>Gets the tracks stored in this GPX document.</p></div>
<dl className="notes">
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

</div>
</div>



</div>
`
}</HTMLBlock>
