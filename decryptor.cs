
using System;
using System.IO;
using System.Text;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;
using System.Security.Cryptography;

namespace Rextester
{
    public class Program
    {
        
        public static byte[] StringToByteArray(string hex) {
        return Enumerable.Range(0, hex.Length)
                         .Where(x => x % 2 == 0)
                         .Select(x => Convert.ToByte(hex.Substring(x, 2), 16))
                         .ToArray();
        }
         public static byte[] EncryptPasswd(string password)
        {
        byte[] array = Encoding.UTF8.GetBytes(password);
        array = SHA256.Create().ComputeHash(array);
        return array;

        }
        public static byte[] AES_DEncrypt(byte[] bytesToBeEncrypted, byte[] passwordBytes)
        {
            byte[] result = null;
            byte[] salt = new byte[]
            {
                1,
                8,
                3,
                6,
                2,
                4,
                9,
                7
            };
            using (MemoryStream memoryStream = new MemoryStream())
            {
                using (RijndaelManaged rijndaelManaged = new RijndaelManaged())
                {
                    rijndaelManaged.KeySize = 256;
                    rijndaelManaged.BlockSize = 128;
                    Rfc2898DeriveBytes rfc2898DeriveBytes = new Rfc2898DeriveBytes(passwordBytes, salt, 1000);
                    rijndaelManaged.Key = rfc2898DeriveBytes.GetBytes(rijndaelManaged.KeySize / 8);
                    rijndaelManaged.IV = rfc2898DeriveBytes.GetBytes(rijndaelManaged.BlockSize / 8);
                    rijndaelManaged.Mode = CipherMode.CBC;
                    using (CryptoStream cryptoStream = new CryptoStream(memoryStream, rijndaelManaged.CreateDecryptor(), CryptoStreamMode.Write))
                    {
                        cryptoStream.Write(bytesToBeEncrypted, 0, bytesToBeEncrypted.Length);
                        cryptoStream.Close();
                    }
                    result = memoryStream.ToArray();
                }
            }
            return result;
        }


  
        public static void Main(string[] args)
        {
            
            string input = "a53b8db46ae3e9d9b8d344a1210b54abc2033161becde81df6a129325b1d3442";
            byte[] enc = StringToByteArray(input);
            
            string hex_passwd = "084b988baa7c8d98cda90c5fe603c560";
            byte[] passwd = EncryptPasswd(hex_passwd);
            
            string path = args[0];
  
            // Calling the ReadAllBytes() function
            byte[] enc_file = File.ReadAllBytes(path);
                
                
            //Your code goes here
            
            byte[] res = AES_DEncrypt(enc_file, passwd);
            
            
            //byte[] res = new byte[]{70, 80};
            Console.WriteLine(BitConverter.ToString(res));
        }
    }
}