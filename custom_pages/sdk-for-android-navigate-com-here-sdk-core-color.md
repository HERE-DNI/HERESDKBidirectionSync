---
title: "Color (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-core-color"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- Color.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.core</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.core.Color</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">Color</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>Represents a color value.</p>
<p>The class is compatible with the native package <code>android.graphics</code> and
 replaces native class <code>Color</code>.</p>
<h3>Usage example:</h3>
<pre className="prettyprint">
 import com.here.sdk.core.Color;
 import static android.graphics.Color.BLUE;
 import static android.graphics.Color.green;

 // Convert native colors to HERE color.
 Color blue = Color.valueOf(android.graphics.Color.BLUE);
 Color anotherColor = Color.valueOf(0.25f, 0.5f, 0.75f, 0.9f); //ARGB
 // Retrieve the blue color component.
 float blueColorValue = anotherColor.blue(); // = 0.9f
 // Convert back to a native color component with the range [0,255].
 int greenColorValue = android.graphics.Color.green(anotherColor.toArgb()); // = 230
 </pre></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section className="method-summary" id="method-summary">

<div id="method-summary-table">


</div>
<div className="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section className="details">
<ul className="details-list">
<!-- ============ METHOD DETAIL ========== -->
<li>
<section className="method-details" id="method-detail">

<ul className="member-list">
<li>
<section className="detail" id="valueOf(float,float,float)">
<h3>valueOf</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a></span> <span className="element-name">valueOf</span><wbr/><span className="parameters">(float red,
 float green,
 float blue)</span></div>
<div className="block">Creates a new opaque color from individual RGB components.</div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>red</code> - <p>the value of red component [0,1]</p></dd>
<dd><code>green</code> - <p>the value of green component [0,1]</p></dd>
<dd><code>blue</code> - <p>the value of blue component [0,1]</p></dd>
<dt>Returns:</dt>
<dd>a new Color instance from given components.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="valueOf(float,float,float,float)">
<h3>valueOf</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a></span> <span className="element-name">valueOf</span><wbr/><span className="parameters">(float red,
 float green,
 float blue,
 float alpha)</span></div>
<div className="block">Creates a new color from individual RGBA components.</div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>red</code> - <p>the value of red component [0,1]</p></dd>
<dd><code>green</code> - <p>the value of green component [0,1]</p></dd>
<dd><code>blue</code> - <p>the value of blue component [0,1]</p></dd>
<dd><code>alpha</code> - <p>the value of alpha component [0,1]</p></dd>
<dt>Returns:</dt>
<dd>a new Color instance from given components.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="valueOf(int)">
<h3>valueOf</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a></span> <span className="element-name">valueOf</span><wbr/><span className="parameters">(@ColorInt
 int color)</span></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>color</code> - ARGB color int</dd>
<dt>Returns:</dt>
<dd>a new Color instance from color int.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="red()">
<h3>red</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">float</span> <span className="element-name">red</span>()</div>
<dl className="notes">
<dt>Returns:</dt>
<dd>value of red component in range [0,1]</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="green()">
<h3>green</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">float</span> <span className="element-name">green</span>()</div>
<dl className="notes">
<dt>Returns:</dt>
<dd>value of green component in range [0,1]</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="blue()">
<h3>blue</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">float</span> <span className="element-name">blue</span>()</div>
<dl className="notes">
<dt>Returns:</dt>
<dd>value of blue component in range [0,1]</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="alpha()">
<h3>alpha</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">float</span> <span className="element-name">alpha</span>()</div>
<dl className="notes">
<dt>Returns:</dt>
<dd>value of alpha component in range [0,1]</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="toArgb()">
<h3>toArgb</h3>
<div className="member-signature"><span className="annotations">@ColorInt
</span><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">toArgb</span>()</div>
<div className="block">Converts this color to an ARGB color int.</div>
<dl className="notes">
<dt>Returns:</dt>
<dd>ARGB color int</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="toString()">
<h3>toString</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">toString</span>()</div>
<dl className="notes">
<dt>Overrides:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a></code> in class <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="equals(java.lang.Object)">
<h3>equals</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">equals</span><wbr/><span className="parameters">(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</span></div>
<dl className="notes">
<dt>Overrides:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a></code> in class <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="hashCode()">
<h3>hashCode</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">hashCode</span>()</div>
<dl className="notes">
<dt>Overrides:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a></code> in class <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
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
