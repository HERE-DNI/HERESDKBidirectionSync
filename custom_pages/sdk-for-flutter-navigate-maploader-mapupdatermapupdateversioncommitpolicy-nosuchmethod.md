---
title: "noSuchMethod method"
slug: "sdk-for-flutter-navigate-maploader-mapupdatermapupdateversioncommitpolicy-nosuchmethod"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- noSuchMethod.html -->


<div>
<h1>noSuchMethod method</h1></div>

dynamic
noSuchMethod(<ol class="parameter-list single-line"> <li>Invocation invocation</li>
</ol>)

      <div class="features">inherited</div>


<p>Invoked when a nonexistent method or property is accessed.</p>
<p>A dynamic member invocation can attempt to call a member which
doesn't exist on the receiving object. Example:</p>
<pre class="language-dart"><code class="language-dart">dynamic object = 1;
object.add(42); // Statically allowed, run-time error
</code></pre>
<p>This invalid code will invoke the <code>noSuchMethod</code> method
of the integer <code>1</code> with an <code>Invocation</code> representing the
<code>.add(42)</code> call and arguments (which then throws).</p>
<p>Classes can override <code>noSuchMethod</code> to provide custom behavior
for such invalid dynamic invocations.</p>
<p>A class with a non-default <code>noSuchMethod</code> invocation can also
omit implementations for members of its interface.
Example:</p>
<pre class="language-dart"><code class="language-dart">class MockList&lt;T&gt; implements List&lt;T&gt; {
  noSuchMethod(Invocation invocation) {
    log(invocation);
    super.noSuchMethod(invocation); // Will throw.
  }
}
void main() {
  MockList().add(42);
}
</code></pre>
<p>This code has no compile-time warnings or errors even though
the <code>MockList</code> class has no concrete implementation of
any of the <code>List</code> interface methods.
Calls to <code>List</code> methods are forwarded to <code>noSuchMethod</code>,
so this code will <code>log</code> an invocation similar to
<code>Invocation.method(#add, [42])</code> and then throw.</p>
<p>If a value is returned from <code>noSuchMethod</code>,
it becomes the result of the original invocation.
If the value is not of a type that can be returned by the original
invocation, a type error occurs at the invocation.</p>
<p>The default behavior is to throw a <code>NoSuchMethodError</code>.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">@pragma("vm:entry-point")
@pragma("wasm:entry-point")
external dynamic noSuchMethod(Invocation invocation);</code></pre>

 



</div>
`
}</HTMLBlock>
