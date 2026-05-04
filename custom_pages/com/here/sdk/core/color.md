---
title: "Color (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestcolor"
hidden: false
---

Package [com.here.sdk.core](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class Color

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.core.Color
------------------------------------------------------------------------
public final class Color extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Represents a color value.

The class is compatible with the native package `android.graphics` and replaces native class `Color`.

### Usage example:

``` prettyprint
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

```

## Method Summary

  All Methods
  Static Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `float`

  [alpha](#alpha())`()`

  `float`

  [blue](#blue())`()`

  `boolean`

  [equals](#equals(java.lang.Object))`(`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)` obj)`

  `float`

  [green](#green())`()`

  `int`

  [hashCode](#hashCode())`()`

  `float`

  [red](#red())`()`

  `int`

  [toArgb](#toArgb())`()`

Converts this color to an ARGB color int.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [toString](#toString())`()`

  `static `[`Color`](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core")

  [valueOf](#valueOf(float,float,float))`(float red, float green, float blue)`

Creates a new opaque color from individual RGB components.

`static `[`Color`](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core")

  [valueOf](#valueOf(float,float,float,float))`(float red, float green, float blue, float alpha)`

Creates a new color from individual RGBA components.

`static `[`Color`](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core")

  [valueOf](#valueOf(int))`(int color)`

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Method Details

### valueOf

@NonNull public static [Color](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core") valueOf(float red, float green, float blue)

    Creates a new opaque color from individual RGB components.
Parameters:
    `red` -

    the value of red component \[0,1\]

    `green` -

    the value of green component \[0,1\]

    `blue` -

    the value of blue component \[0,1\]

    Returns:
    a new Color instance from given components.

### valueOf

@NonNull public static [Color](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core") valueOf(float red, float green, float blue, float alpha)

    Creates a new color from individual RGBA components.
Parameters:
    `red` -

    the value of red component \[0,1\]

    `green` -

    the value of green component \[0,1\]

    `blue` -

    the value of blue component \[0,1\]

    `alpha` -

    the value of alpha component \[0,1\]

    Returns:
    a new Color instance from given components.

### valueOf

@NonNull public static [Color](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core") valueOf(@ColorInt int color)
Parameters:
    `color` - ARGB color int

    Returns:
    a new Color instance from color int.

### red

public float red()
Returns:
    value of red component in range \[0,1\]

### green

public float green()
Returns:
    value of green component in range \[0,1\]

### blue

public float blue()
Returns:
    value of blue component in range \[0,1\]

### alpha

public float alpha()
Returns:
    value of alpha component in range \[0,1\]

### toArgb

@ColorInt public int toArgb()

    Converts this color to an ARGB color int.
Returns:
    ARGB color int

### toString

@NonNull public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) toString()
Overrides:
    [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
