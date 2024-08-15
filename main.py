#include "U8glib.h"
#define LDR_PIN 2


U8GLIB_SSD1306_128X64 u8g(U8G_I2C_OPT_DEV_0 | U8G_I2C_OPT_NO_ACK | U8G_I2C_OPT_FAST); // Fast I2C / TWI

int progress = 0;
void setup() {
  pinMode(LDR_PIN, INPUT);
  Serial.begin(115200);
  u8g.setFont(u8g_font_tpssb);
  u8g.setColorIndex(1);

}

void loop() {
  if (digitalRead(LDR_PIN) == LOW) {
    Serial.println("Light!");
  } else {
    Serial.println("Dark!");
  }
  

  u8g.firstPage();
  do {
    u8g.drawStr(25, 50, "Progress Bar");
    u8g.drawFrame(0, 10, 128, 20);
    u8g.drawBox(10, 15, progress, 10);
  } while ( u8g.nextPage() );

  if (progress < 108) {
    progress++;
  } else {
    progress = 0;
  }
  delay(100);
}
