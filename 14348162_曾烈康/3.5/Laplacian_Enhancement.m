function Laplacian_Enhancement()
    close all
    fi=imread('Fig3.40(a).jpg');
    figure,imshow(fi),title('ԭʼͼ��');    %��ӡԭʼͼ��

    mask = [-1,-1,-1;-1,8,-1;-1,-1,-1];     %mask��ʾ��ģ����
    imLF = BlurFilter(fi,mask);
    figure,imshow(imLF),title('������˹�˲���ͼ��');
    imwrite(imLF,'Fig3.40(a)mask.jpg');
    
    imLE = double(fi)+double(imLF);
    imLE = uint8(imLE);
    figure,imshow(imLE),title('������˹��ǿ��ͼ��');
    imwrite(imLE,'Fig3.40(a)Lap.jpg'); 
    
function imLF = BlurFilter(fi,mask)         %�����˲���ľ���
    im = double(fi);
    [m,n] = size(fi);
    imLF = zeros(m,n);
    for x = 2:m-1              %��ÿ�����ص㣬����ģ�����Ȩ�����Χ������ֵ
        for y = 2:n-1
            imLF(x,y)=im(x-1,y-1)*mask(1,1)+im(x-1,y)*mask(1,2)+im(x-1,y+1)*mask(1,3)...          
                +im(x,y-1)*mask(2,1)+im(x,y)*mask(2,2)+im(x,y+1)*mask(2,3)...        
                +im(x+1,y-1)*mask(3,1)+im(x+1,y)*mask(3,2)+im(x+1,y+1)*mask(3,3);
        end
    end